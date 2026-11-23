# Dart box PETG (process) — file `Dart_Box_PETG_N4Plus.json`

- **Parent:** `0.24mm Draft @Elegoo N4Plus 0.4 nozzle`
- **Status:** **missing**. It was never imported into ElegooSlicer and isn't in Downloads (export of 2026-11-23); only the PLA test version exists. This note is the full record of the intended settings. Rebuild the preset before the PETG print, ideally as a Rev B preset that includes the recommendations below.
- **Used by:** dart box, final build in PETG
- **Origin:** [Printing with PLA advice](https://claude.ai/chat/55c2e0c1-71c2-41d6-a611-69e7294c37bd); Rev B print notes in [Dart box rework in Fusion 360](https://claude.ai/chat/d8768692-00b6-4a82-bbe1-549cfc11935a)

## Purpose
Solid, double-walled heated dart box with long bridges and no supports.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Layer height | 0.24 | **0.25 mm** | The box logos are built from pixel rows exactly 0.25 mm tall (~3,500 of them). At 0.25 each layer lands on one row; at 0.24 a row doubles or drops every ~25 layers (banding). |
| Wall loops | 2 | 5 | Makes the 2.5 mm skins fully solid. |
| Supports | off | off + don't support bridges | Your earlier copy had supports on, which put supports inside the walls. |
| Bridges | 50 mm/s | 25 mm/s, thick bridges on | Foam-cavity ties and the 132 mm span over the drawer opening. |
| Seam | aligned | back | Keeps it off the front and the logo sides. |
| Elephant-foot comp. | 0.10 | 0.15 | The bottom edge is the base interface (lip pockets, clip notch). |
| Brim | 5 mm | 5 mm outer only | Corner lift on a 279 mm footprint. |
| Wall speeds outer / inner | 160 / 200 | 80 / 120 | PETG bonds and bridges better slower. |
| Accel default / outer wall | 5000 | 3000 / 2000 | A heavy part on a moving bed. |
| Infill / solid / top / travel | — | 150 / 120 / 80 / 300 |  |

## Filament side (not in this preset)
- PETG profile with bridge fan 100 %; keep its max volumetric speed.
- Smooth PEI: thin, even glue stick as a release agent. Textured PEI is fine bare.

## Rev B recommendations not yet in any preset
- Box top: supports on, painted enforcer under the drawer header only, threshold ~10°, top Z 0.2 mm, 2 interface layers, not build-plate-only.
- Brim 8 mm outer only, 0.1 mm gap. Part fan off for layers 1–3, full by layer 6 (filament). Draft shield or an enclosure.
- Bed 80 °C for PETG; heat-soak 10 min, then mesh hot. Clean the PEI with dish soap, then IPA.
- Lid (logo face down): 0.2 mm layers for at least the first 1 mm, EF comp 0, first layer 20 mm/s at 0.42 mm wide, Arachne with 25 % minimum feature size.
- Decide whether these become a `Dart Box Rev B` preset or stay as per-object settings in the .3mf.
