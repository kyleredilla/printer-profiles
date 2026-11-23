# Siraya TPU Air - Dense 240 (filament)

- **Parent:** `Elegoo TPU 95A @EN4 Series`
- **Status:** active
- **Used by:** R66 and R22 stab covers (body)
- **Origin:** [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40); flow calibration also in [R22 horizontal stabilizer cover](https://claude.ai/chat/66a8d21c-e0f8-4cdc-9447-bed9be27920d)

## Purpose
Base preset for Siraya Tech Flex TPU Air printed dense (less foaming) on the Neptune 4 Plus. Foamed sections are made by switching temperature and flow mid-print with layer-slider G-code, not by a second preset.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Nozzle temp (first / other layers) | stock TPU | 240 / 240 °C | Siraya datasheet: 240 °C gives ~78A, 10.3 MPa, 629 % elongation vs. 68A, 5.0 MPa at 260 °C. Dense is tougher for cuffs and lips. |
| Flow ratio | — | **0.53** (created as 0.88) | Created at Siraya's 85–90 % for 230–240 °C. Hollow 20×20×10 mm cube tests gave 0.53 for the target wall: new flow = current × 0.84 ÷ measured wall (mm), with 0.84 mm = 2 × 0.42 mm lines. |
| Bed (hot plate / textured, all layers) | stock | 40 °C | Siraya range 30–45 °C. Use glue stick as a release agent on PEI; let the bed cool fully before removing parts. |
| Fan min / max | stock | 100 / 100 % | Siraya recommends full cooling. |
| Fan off for first N layers | — | 1 | First-layer adhesion. |
| Retraction length / speed | stock | 0 / 0 | Siraya: normal retraction doesn't work well with foaming filament. |
| Z-hop | stock | 0 | With no retraction, a hop only adds strings. |
| Max volumetric speed | stock | 4 mm³/s | Soft TPU in a direct drive: keeps the extruder from slipping (~30–45 mm/s at 0.2 mm layers). |
| Min layer time (slow down for cooling) | stock | 8 s | Small layers need time to set before the next one. |
| Nozzle temp range | stock | 230–270 °C | Siraya's published range. |

## Mid-print temperature/flow switching (lives in the .3mf, not here)
- R66 cover: at 5.0 mm `M104 S260` + `M221 S66` (foam); at 137 mm `M104 S240` + `M221 S100` (dense cuff).
- M221 % = (flow at the foam temperature) ÷ (this preset's flow). Recalculate it whenever either flow changes; with 0.53 here the old S66 is wrong.

## To verify
- **Verified 2026-11-23 from the slicer:** flow 0.53. The fan, cooling and min-layer-time keys were dropped when the slicer saved, because they equal the parent (Elegoo TPU 95A @EN4 Series). They're inherited, not lost.
- `filament_density` is **0.88**, which looks like the flow value pasted into the wrong field (TPU is ~1.2 g/cm³). It only affects weight and cost estimates. Fix it to ~1.2 in the slicer and pull again.
- Temperature-tower results (215–235 °C, see Surface 230) suggest stringing comes from moisture or seam placement, not temperature. Dry the spool at 70–80 °C for 4–6 h.

## Import lessons
- Two earlier attempts failed: a generic parent name (`Elegoo Generic TPU`) and a missing ElegooSlicer header. This file copies the format of your own export (`from: User`, `filament_settings_id`, `version 1.5.3.5`).
