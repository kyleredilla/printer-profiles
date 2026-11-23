# printer-profiles

Version-controlled slicer profiles for the shop's 3D printers. Git is the source of truth;
the slicers are where profiles get *used*.

| Printer | Slicer | Profile folders |
|---|---|---|
| Elegoo Neptune 4 Plus (Klipper) | ElegooSlicer 1.5.3.5 (OrcaSlicer fork) | `printers/neptune4plus/elegooslicer/{filament,process,machine}` |
| FibreSeeker 3 | Rocket Slicer | `printers/fibreseeker3/rocketslicer/{materials,profiles}` |

`INVENTORY.md` lists every profile, what it's for, its status and where it came from.

## Layout

```
printers/<printer>/<slicer>/...   profiles, one JSON per preset, named after the preset
printers/<printer>/<slicer>/notes/<preset name>.md
                                  why each setting is what it is, open items, origin chat
printers/<printer>/reference/     stock/expanded presets for comparison (never import these)
SUPERSEDED.md                     retired profiles and what replaced them
jobs/<part-name>/                 one folder per real part: NOTES.md + the .3mf project
scripts/profiles.py               pull / ingest / check
tools/                            helper scripts (e.g. splice_inlay G-code splicer)
```

## Rules

1. **Base profiles vs. job tweaks.** Keep a small set of base profiles. A one-off tweak for a
   single print lives in that job's `.3mf` (it embeds the full settings) plus a line in its
   `NOTES.md`. Promote it to a profile only when you reuse it.
2. **Naming.** Say what it's for:
   - ElegooSlicer process: `<layer>mm <Purpose> @Elegoo N4Plus 0.4 nozzle`
   - ElegooSlicer filament: `<Brand> <Material> - <Variant>` (e.g. `Siraya TPU Air - Dense 240`)
   - Rocket Slicer: `<Material> <layer> mm - <Purpose>` (e.g. `FS PET GF 0.2 mm - vacuum adapter`)
3. **The commit message is the "why".** e.g. `TPU Air Dense 240: flow 0.88 -> 0.53 (hollow-cube calibration)`.
4. **Every profile gets a row in INVENTORY.md and a notes file.** Status is one of `active`, `testing`,
   `superseded`, `reference`. When you change a setting, update its row in the notes table
   (old → new, why) in the same commit.
5. **Retire, don't delete.** Set status to `superseded` and note what replaced it. Git keeps the history either way.

## Workflow

```bash
# 1. Pull current user presets out of the slicers into the repo
python3 scripts/profiles.py pull

# 2. Or drop in files you exported / downloaded (auto-routed by type)
python3 scripts/profiles.py ingest ~/Downloads/*.json

# 3. Sanity-check everything (valid JSON, names, Rocket material links)
python3 scripts/profiles.py check

# 4. Review and commit
git diff
git add -A && git commit -m "Dart box PETG: bridge speed 25 -> 20 (sagging over drawer)"
```

To put a profile **into** a slicer, use the slicer's own import (ElegooSlicer: File → Import →
Import Configs; Rocket Slicer: material / profile import). The script never writes into the
slicers' folders.

### Slicer folder locations

Set in `scripts/sync_config.json`. ElegooSlicer on macOS keeps user presets under
`~/Library/Application Support/ElegooSlicer/user/<id>/{filament,process,machine}`; `pull`
finds the `<id>` folder itself. Rocket Slicer's storage location is not confirmed yet, so its
entry starts empty: export from Rocket Slicer and use `ingest` until it's filled in.

## Slicer gotchas (learned the hard way)

**ElegooSlicer**
- Imports fail unless the file matches ElegooSlicer's own export format: `"from": "User"`,
  `print_settings_id` / `filament_settings_id` equal to the name, a `version`, and an
  `inherits` that exactly matches an installed system preset
  (e.g. `0.20mm Standard @Elegoo N4Plus 0.4 nozzle`, `Elegoo TPU 95A @EN4 Series`).
- Retraction, fan and minimum layer time live in the **filament** preset, not the process preset.
- `.info` sidecar files are ignored by git (timestamps only).

**Rocket Slicer**
- Built-in templates can't be edited; copy one first.
- A print profile's `ProfileMaterials[].PlasticId` must equal the material's `Id`, or the profile
  won't show under that material.
- Profile files hold three mode blocks (`SpeedyProfiles` = plastic only, `ReinForcedProfiles`,
  `FortifiedProfiles`). Only the block with `ProfileEnable: true` matters.
- Edited files keep the original internal IDs, so importing **overwrites** the entry it was
  copied from. Make a fresh copy in the slicer first if you want to keep the original.
- Retraction is in two places: material (`RetractionSpeed` / `RetractionLengthOnTravel`) and
  profile (`DoRetractOnLayerChange`).
- Pressure advance is a `SET_PRESSURE_ADVANCE ... ADVANCE=` line inside the profile's start G-code.
