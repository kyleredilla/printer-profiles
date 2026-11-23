# Profile inventory

Status: `active` · `testing` · `legacy` · `missing` · `superseded`. Each profile's reasoning is in
`printers/<printer>/<slicer>/notes/<type>/`; retired profiles that aren't committed are in `SUPERSEDED.md`.
Last synced from the slicers: **2026-11-23** (ElegooSlicer user presets + Downloads exports).

## Neptune 4 Plus — ElegooSlicer 1.5.3.5

### Filament presets

| Name | Parent | Purpose / key settings | Status | Origin |
|---|---|---|---|---|
| Siraya TPU Air - Dense 240 | Elegoo TPU 95A @EN4 Series | Dense TPU Air base for stab covers. 240 °C, **flow 0.53** (cube-calibrated), bed 40, no retraction, 4 mm³/s. | active | [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40) |
| Siraya TPU Air - Dense 240 Logo | Elegoo TPU 95A @EN4 Series | Logo-only: flow 0.50, retraction 0.8 mm @ 25 (deretract 15), wipe 1.5 mm, Z-hop 0.2. | testing | [R22 horizontal stabilizer cover](https://claude.ai/chat/66a8d21c-e0f8-4cdc-9447-bed9be27920d) |
| Siraya TPU Air - Surface 230 | Elegoo TPU 95A @EN4 Series | splice_inlay v4 surface/logo layers. 230 °C, **flow 0.72** (changed by hand from 0.60; reason not recorded), retraction 0.8, wipe 1.5, Z-hop 0.2. | testing | [Multicolor TPU logo printing](https://claude.ai/chat/a6701a89-15db-4018-8db1-fb87bd4eb8a4) |
| Elegoo PLA+ @EN4 - Overhang Cool 60 | Elegoo PLA+ @EN4 Series | Overhang/bridge/support-interface fan 60 %, fan off for layers 1–3, full at 6. For the dart box base back plate. | active | [Dart box rework in Fusion 360](https://claude.ai/chat/d8768692-00b6-4a82-bbe1-549cfc11935a) |
| Siraya TPU Air | Elegoo TPU 95A @EN4 Series | Your Sept experiment: 260 °C foamed, flow 0.6, no retraction. | legacy | your own (2026-09-12) |

### Process presets

| Name | Parent | Purpose / key settings | Status | Origin |
|---|---|---|---|---|
| Siraya TPU Air - Stab Cover | 0.20mm Standard @Elegoo N4Plus 0.4 nozzle | TPU covers: 5 walls, gyroid 18 %, random + scarf seam, avoid crossing walls, 1 skirt, no supports, 20–30 mm/s. | active | [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40) |
| Siraya TPU Air - Stab Cover Surface | 0.20mm Standard @Elegoo N4Plus 0.4 nozzle | Stab Cover for spliced surface/logo slices: travel 200, no skirt. Layer heights must match Stab Cover. | testing | [Multicolor TPU logo printing](https://claude.ai/chat/a6701a89-15db-4018-8db1-fb87bd4eb8a4) |
| 0.24mm Tall Part - Adapter RevB @Elegoo N4Plus 0.4 nozzle | 0.24mm Draft @Elegoo N4Plus 0.4 nozzle | Tall PETG parts: 3 walls, organic tree supports, 10 mm brim, reduced accel, walls 80/120. | active | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| 0.25mm Dart Box PLA test @Elegoo N4Plus 0.4 nozzle | 0.24mm Draft @Elegoo N4Plus 0.4 nozzle | Dart box fit tests in PLA: 0.25 mm layers, 5 walls, no supports, bridges 35, walls 120/180. | testing | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| Dart box PETG (`Dart_Box_PETG_N4Plus.json`) | 0.24mm Draft @Elegoo N4Plus 0.4 nozzle | Final PETG dart box. **Never saved; no JSON exists.** The full settings record is in its note. | missing | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| Siraya TPU Air | 0.20mm Standard @Elegoo N4Plus 0.4 nozzle | Your Sept experiment: TPU speeds (20/30), supports on. | legacy | your own (2026-09-12) |
| 0.20mm Standard @Elegoo N4Plus 0.4 nozzle - Copy | 0.20mm Standard @Elegoo N4Plus 0.4 nozzle | Standard with supports on. Purpose unrecorded. | legacy | your own (2026-06-21) |

### Reference (not importable; not committed yet)

| File | What | Origin |
|---|---|---|
| Full_0.24mm_Draft_N4Plus_REFERENCE.json | Stock 0.24 Draft, fully expanded | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| Full_0.20mm_Standard_N4Plus_REFERENCE.json | Stock 0.20 Standard, fully expanded | same |

## FibreSeeker 3 — Rocket Slicer

No Rocket Slicer data folder was found on the Mac; these come from exported files in Downloads.
Export again from Rocket Slicer whenever a preset changes and run `ingest`.

### Plastic materials

| Name | Copied from | Purpose / key settings | Status | Origin |
|---|---|---|---|---|
| Siraya Tech TPU Air - FS3 250C | PETG template | TPU Air, plastic only. 250 °C, flow 0.60, bed 40, no retraction or Z-hop (incl. tool change), fan 100, 8 mm³/s. | active | [Fiberseeker TPU profile setup](https://claude.ai/chat/4eea174a-e2b5-4b56-9399-7a021f574900) |

### Print profiles

| Name | Material | Purpose / key settings | Status | Origin |
|---|---|---|---|---|
| Siraya Tech TPU Air 0.2 mm | TPU Air - FS3 250C | Speedy. 20–40 mm/s, no layer-change retract or Z-hop, clog sensor off for the job (start/end G-code). PA still 0.06. | active | [TPU Air filament setup](https://claude.ai/chat/63882b13-8f59-4af6-aecd-04838b89ac69) → [Fiberseeker TPU profile setup](https://claude.ai/chat/4eea174a-e2b5-4b56-9399-7a021f574900) |
| FS PET GF 0.2 mm - vacuum adapter | PET GF (`05530460…`, not in repo) | Speedy. 8 walls, walls 80/120, 12-loop brim, 5 bottom layers. Replaced your "FS PET GF 0.2 mm" copy; stock template untouched. | active | [Vacuum hose adapter design](https://claude.ai/chat/84a5679a-ee14-4c19-96aa-f3e2d681614c) |

## Related tools (not profiles)

| Item | Location now | Notes |
|---|---|---|
| splice_inlay_v4.py | Mac: `~/base/print_splicing/R22_stab_cover/` | Single-nozzle two-colour inlay G-code splicer (bottom mode, `--body-upper`). Candidate for `tools/`. |
