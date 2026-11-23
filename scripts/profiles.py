#!/usr/bin/env python3
"""Manage slicer profiles in this repo.

  python3 scripts/profiles.py pull            copy user presets out of the slicers (see sync_config.json)
  python3 scripts/profiles.py ingest FILE...  file exported/downloaded profiles into the right folder
  python3 scripts/profiles.py check           validate every profile in the repo

Files are routed by content, not by filename:
  ElegooSlicer filament / process / machine  -> printers/neptune4plus/elegooslicer/<type>/
  Rocket Slicer plastic material             -> printers/fibreseeker3/rocketslicer/materials/
  Rocket Slicer print profile                -> printers/fibreseeker3/rocketslicer/profiles/

Nothing is ever written into a slicer's own folders. Python 3.8+, standard library only.
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG = os.path.join(ROOT, "scripts", "sync_config.json")
ELEGOO_DIR = os.path.join(ROOT, "printers", "neptune4plus", "elegooslicer")
ROCKET_DIR = os.path.join(ROOT, "printers", "fibreseeker3", "rocketslicer")
ROCKET_MODES = ("SpeedyProfiles", "ReinForcedProfiles", "FortifiedProfiles")


# ---------------------------------------------------------------- detection
def first(v):
    return v[0] if isinstance(v, list) and v else v


def classify(d):
    """Return (kind, name) or (None, None). kind is e.g. 'elegoo/filament', 'rocket/material'."""
    if not isinstance(d, dict):
        return None, None
    if "filament_settings_id" in d or d.get("type") == "filament":
        return "elegoo/filament", d.get("name") or first(d.get("filament_settings_id"))
    if "print_settings_id" in d or d.get("type") == "process":
        return "elegoo/process", d.get("name") or first(d.get("print_settings_id"))
    if "printer_settings_id" in d or d.get("type") == "machine":
        return "elegoo/machine", d.get("name") or first(d.get("printer_settings_id"))
    data = d.get("Data")
    if isinstance(data, dict) and ("PlasticType" in data or "ExtrusionMultiplierP" in data):
        return "rocket/material", data.get("Name")
    if any(k in d for k in ROCKET_MODES):
        grp = d.get("ProfileGroup") or {}
        return "rocket/profile", grp.get("Name") or d.get("Name")
    return None, None


def rocket_enabled_block(d):
    for mode in ROCKET_MODES:
        for blk in d.get(mode) or []:
            if isinstance(blk, dict) and blk.get("ProfileEnable"):
                return blk
    return None


def dest_dir(kind):
    slicer, typ = kind.split("/")
    if slicer == "elegoo":
        return os.path.join(ELEGOO_DIR, typ)
    return os.path.join(ROCKET_DIR, "materials" if typ == "material" else "profiles")


def safe_filename(name):
    return re.sub(r'[\\/:*?"<>|]+', "-", name).strip() + ".json"


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- writing
def file_into_repo(src, d=None, quiet=False):
    """Copy one profile into the repo. Returns 'new' | 'changed' | 'same' | 'skipped'."""
    try:
        d = d if d is not None else load(src)
    except (OSError, ValueError) as e:
        print(f"  skip  {src}: not valid JSON ({e})")
        return "skipped"
    kind, name = classify(d)
    if not kind:
        print(f"  skip  {src}: not a recognised ElegooSlicer / Rocket Slicer profile")
        return "skipped"
    name = name or os.path.splitext(os.path.basename(src))[0]
    out = os.path.join(dest_dir(kind), safe_filename(name))
    os.makedirs(os.path.dirname(out), exist_ok=True)

    raw = open(src, encoding="utf-8").read()
    if kind.startswith("rocket/") and raw.count("\n") < 3:
        # Rocket Slicer exports can be one long line; pretty-print so git diffs are readable.
        raw = json.dumps(d, indent=2, ensure_ascii=False) + "\n"

    old = open(out, encoding="utf-8").read() if os.path.exists(out) else None
    status = "new" if old is None else ("same" if old == raw else "changed")
    if status != "same":
        with open(out, "w", encoding="utf-8") as f:
            f.write(raw)
    if not quiet or status != "same":
        print(f"  {status:7} {kind:16} {os.path.relpath(out, ROOT)}")
    return status


# ---------------------------------------------------------------- commands
def cmd_pull(_args):
    if not os.path.exists(CONFIG):
        sys.exit(f"Missing {CONFIG}")
    cfg = load(CONFIG)
    counts = {}

    base = os.path.expanduser(cfg.get("elegooslicer_dir") or "")
    if base and os.path.isdir(base):
        users = sorted(u for u in glob.glob(os.path.join(base, "user", "*"))
                       if any(os.path.isdir(os.path.join(u, t)) for t in ("filament", "process", "machine")))
        if not users:
            print(f"ElegooSlicer: no user preset folders under {base}/user")
        if len(users) > 1:
            print(f"ElegooSlicer: {len(users)} user folders found, pulling all: {[os.path.basename(u) for u in users]}")
        for u in users:
            print(f"ElegooSlicer  {u}")
            for typ in ("filament", "process", "machine"):
                for p in sorted(glob.glob(os.path.join(u, typ, "*.json"))):
                    s = file_into_repo(p, quiet=True)
                    counts[s] = counts.get(s, 0) + 1
    else:
        print(f"ElegooSlicer: folder not found ({base or 'not set'}), skipping")

    for rdir in cfg.get("rocketslicer_dirs") or []:
        rdir = os.path.expanduser(rdir)
        if not os.path.isdir(rdir):
            print(f"Rocket Slicer: folder not found ({rdir}), skipping")
            continue
        print(f"Rocket Slicer {rdir}")
        for p in sorted(glob.glob(os.path.join(rdir, "**", "*.json"), recursive=True)):
            try:
                d = load(p)
            except (OSError, ValueError):
                continue
            if classify(d)[0]:
                s = file_into_repo(p, d, quiet=True)
                counts[s] = counts.get(s, 0) + 1
    if not cfg.get("rocketslicer_dirs"):
        print("Rocket Slicer: no folder configured yet - export profiles and use 'ingest'")

    print("\nSummary:", ", ".join(f"{v} {k}" for k, v in sorted(counts.items())) or "nothing found")
    print("Next: python3 scripts/profiles.py check, then git diff")


def cmd_ingest(args):
    for p in args.files:
        file_into_repo(p)
    print("Next: add/update rows in INVENTORY.md, then commit.")


def cmd_check(_args):
    problems, warnings = [], []
    inventory = open(os.path.join(ROOT, "INVENTORY.md"), encoding="utf-8").read()
    files = sorted(glob.glob(os.path.join(ROOT, "printers", "**", "*.json"), recursive=True))
    rocket_material_ids, rocket_links = set(), []

    for p in files:
        rel = os.path.relpath(p, ROOT)
        if f"{os.sep}reference{os.sep}" in p:
            continue
        try:
            d = load(p)
        except ValueError as e:
            problems.append(f"{rel}: invalid JSON - {e}")
            continue
        kind, name = classify(d)
        if not kind:
            warnings.append(f"{rel}: not recognised as a profile")
            continue
        if kind.startswith("elegoo/"):
            typ = kind.split("/")[1]
            sid = first(d.get({"filament": "filament_settings_id", "process": "print_settings_id",
                               "machine": "printer_settings_id"}[typ]))
            if sid is not None and sid != d.get("name"):
                problems.append(f"{rel}: name '{d.get('name')}' != settings id '{sid}' (import will fail)")
            if str(d.get("from", "")).lower() != "user":
                warnings.append(f"{rel}: \"from\" is '{d.get('from')}', ElegooSlicer exports use \"User\"")
            if not d.get("inherits"):
                warnings.append(f"{rel}: no 'inherits' - must name an installed system preset exactly")
            if not d.get("version"):
                warnings.append(f"{rel}: no 'version' field")
        elif kind == "rocket/material":
            mid = d["Data"].get("Id") or d.get("Id")
            if mid:
                rocket_material_ids.add(mid)
        elif kind == "rocket/profile":
            blk = rocket_enabled_block(d)
            if not blk:
                warnings.append(f"{rel}: no mode block has ProfileEnable=true")
            # material links are a top-level list; CompositeId entries are fiber, PlasticId entries are plastic
            for m in d.get("ProfileMaterials") or []:
                if isinstance(m, dict) and m.get("PlasticId"):
                    rocket_links.append((rel, "ProfileMaterials", m["PlasticId"]))
        if name and name not in inventory:
            warnings.append(f"{rel}: '{name}' has no row in INVENTORY.md")
        note = os.path.join(os.path.dirname(os.path.dirname(p)), "notes",
                            safe_filename(name or "")[:-5] + ".md")
        if not os.path.exists(note):
            warnings.append(f"{rel}: no notes file ({os.path.relpath(note, ROOT)})")
        if os.path.basename(p) != safe_filename(name or ""):
            warnings.append(f"{rel}: filename doesn't match preset name '{name}'")

    for rel, mode, pid in rocket_links:
        if pid not in rocket_material_ids:
            warnings.append(f"{rel} [{mode}]: PlasticId {pid} is not a material in this repo "
                            "(fine if it's a stock material, otherwise the link is broken)")

    print(f"Checked {len(files)} JSON files.")
    for w in warnings:
        print("  warn ", w)
    for e in problems:
        print("  ERROR", e)
    if not warnings and not problems:
        print("  all good")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("pull").set_defaults(fn=cmd_pull)
    ing = sub.add_parser("ingest")
    ing.add_argument("files", nargs="+")
    ing.set_defaults(fn=cmd_ingest)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
