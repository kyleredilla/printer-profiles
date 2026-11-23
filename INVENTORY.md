# Profile inventory

Status: `active` · `testing` · `superseded` · `reference`. **In repo** = the file is committed here.
Chat links are where each profile was made or last changed.

## Neptune 4 Plus — ElegooSlicer

### Filament presets

| Name | Parent | Purpose / key settings | Status | In repo | Origin |
|---|---|---|---|---|---|
| Siraya TPU Air - Dense 240 | Elegoo TPU 95A @EN4 Series | Dense TPU Air base (R66/R22 stab covers). 240 °C, bed 40, fan 100 (off layer 1), no retraction/Z-hop, 4 mm³/s, 8 s min layer. Created at flow 0.88; later hollow-cube calibration gave **0.53**, so check which value your slicer copy has. | active | no | [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40) |
| Siraya TPU Air - Dense 240 Logo | (Dense 240) | Logo-only variant: adds retraction, wipe and Z-hop to cut stringing on the inlay logo. | testing | no | [R22 horizontal stabilizer cover](https://claude.ai/chat/66a8d21c-e0f8-4cdc-9447-bed9be27920d) |
| Siraya TPU Air - Surface 230 | (Dense 240) | Low-foam surface/logo layers for splice_inlay v4. 230 °C, retract 0.8 mm (25 out / 15 in), wipe 1.5 mm, Z-hop 0.2. **Flow 0.60 is an uncalibrated guess.** | testing | no | [Multicolor TPU logo printing](https://claude.ai/chat/a6701a89-15db-4018-8db1-fb87bd4eb8a4) |
| Siraya TPU Air (dense 240C) — file `TPU Air - filament.json` | Elegoo Generic TPU (wrong parent) | First attempt; never imported. Replaced by Dense 240. | superseded | no — don't add | [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40) |

### Process presets

| Name | Parent | Purpose / key settings | Status | In repo | Origin |
|---|---|---|---|---|---|
| Siraya TPU Air - Stab Cover | 0.20mm Standard @Elegoo N4Plus 0.4 nozzle | TPU stab covers. 5 walls, 5 top/5 bottom, gyroid 18 %, 0.5 mm first-layer width, random seam + scarf, avoid crossing walls, no brim, 1 skirt, supports off, 20–35 mm/s. Dense↔foam switching is layer-slider G-code in the .3mf, not here. | active | no | [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40) |
| Siraya TPU Air - Stab Cover Surface | (Stab Cover) | Stab Cover copy for the surface/logo slice: travel 200, skirt off. Layer heights must match Stab Cover for splicing. | testing | no | [Multicolor TPU logo printing](https://claude.ai/chat/a6701a89-15db-4018-8db1-fb87bd4eb8a4) |
| 0.24mm Tall Part - Adapter RevB @Elegoo N4Plus 0.4 nozzle | 0.24mm Draft @Elegoo N4Plus 0.4 nozzle | Tall PETG part: 3 walls, tree/organic supports (not plate-only), 10 mm outer brim, EF comp 0.15, reduced accel, walls 80/120. | active | no | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| Dart box PETG — file `Dart_Box_PETG_N4Plus.json` | 0.24mm Draft @Elegoo N4Plus 0.4 nozzle | Dart box in PETG: **0.25 mm layers** (logo pixel rows), 5 walls, supports off + don't support bridges, bridges 25 mm/s thick, back seam, EF 0.15, 5 mm brim, walls 80/120, accel 3000/2000. | active | no | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| 0.25mm Dart Box PLA test @Elegoo N4Plus 0.4 nozzle | (Dart box PETG) | PLA fit-test version: walls 120/180, infill 200, bridges 35, accel 4000/2500, travel 400. Rev B notes add: supports only under the drawer header, 8 mm brim. | testing | no | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| TPU Air - process.json | fdm_process_elegoo_common (wrong parent) | First attempt; never imported. Replaced by Stab Cover. | superseded | no — don't add | [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40) |

### Reference (not importable)

| File | What | Origin |
|---|---|---|
| Full_0.24mm_Draft_N4Plus_REFERENCE.json | Stock 0.24 Draft, fully expanded (all 144 settings) | [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd) |
| Full_0.20mm_Standard_N4Plus_REFERENCE.json | Stock 0.20 Standard, fully expanded | same |

## FibreSeeker 3 — Rocket Slicer

### Plastic materials

| Name | Copied from | Purpose / key settings | Status | In repo | Origin |
|---|---|---|---|---|---|
| Siraya Tech TPU Air - FS3 250C | PETG template | TPU Air, plastic-only, right nozzle. 250 °C, flow 0.60, bed 40, no retraction/Z-hop (incl. tool change), fan 100, 8 mm³/s. Flow guide: 240 °C≈0.65–0.70, 260≈0.55, 270≈0.50. | active | no | [Fiberseeker TPU profile setup](https://claude.ai/chat/4eea174a-e2b5-4b56-9399-7a021f574900) |
| Siraya Tech TPU Air (260 °C) | PETG template | First version: 260 °C, flow 0.58, 4 mm³/s. Deleted from the slicer after the FS3 250C import. | superseded | no — don't add | [TPU Air filament setup](https://claude.ai/chat/63882b13-8f59-4af6-aecd-04838b89ac69) |

### Print profiles

| Name | Material link | Purpose / key settings | Status | In repo | Origin |
|---|---|---|---|---|---|
| Siraya Tech TPU Air 0.2 mm (FS3) — file `Siraya_Tech_TPU_Air_0.2_mm_FS3.json` | TPU Air - FS3 250C | Speedy (plastic only). 20–40 mm/s, first layer 20 @ 0.48 mm, no Z-hop / layer-change retract / coast, avoid crossing perimeters, infill flow 1.00, bottom skin width fixed 0.01→0.4. **Start G-code turns off the motion (clog) sensor; end G-code turns it back on.** Pressure advance still PETG 0.06, needs tuning. | active | no | [Fiberseeker TPU profile setup](https://claude.ai/chat/4eea174a-e2b5-4b56-9399-7a021f574900) |
| Siraya Tech TPU Air 0.2 mm (v1) | TPU Air (260 °C) | First version; same internal ID, so the FS3 import overwrote it. | superseded | no — don't add | [TPU Air filament setup](https://claude.ai/chat/63882b13-8f59-4af6-aecd-04838b89ac69) |
| FS PET GF 0.2 mm - vacuum adapter | stock PET GF | Speedy: 8 walls (2 + 6 inner), walls 80/120, brim 12 loops, 5 bottom layers. Kept stock internal IDs, so the import **may have overwritten stock PET GF 0.2 mm**. Check the slicer. Bottom skin width 0.01 left as stock. | active | no | [Vacuum hose adapter design](https://claude.ai/chat/84a5679a-ee14-4c19-96aa-f3e2d681614c) |

## Related tools (not profiles)

| Item | Location now | Notes |
|---|---|---|
| splice_inlay_v4.py | Mac: `~/base/print_splicing/R22_stab_cover/` | Single-nozzle two-colour inlay G-code splicer (bottom mode, `--body-upper`). Candidate for `tools/`. |
