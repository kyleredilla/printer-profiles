# Siraya TPU Air - Stab Cover (process)

- **Parent:** `0.20mm Standard @Elegoo N4Plus 0.4 nozzle`
- **Status:** active
- **Used by:** R66 and R22 stab covers
- **Origin:** [R66 stab cover, elegoo configs](https://claude.ai/chat/643abcae-cc7c-410e-95b6-f6f59364ca40)

## Purpose
Process preset for stretch-fit TPU Air covers: a solid perimeter cuff, light padding inside, slow TPU speeds.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Layer height / first layer | 0.2 | 0.2 mm |  |
| Wall loops | 2 | 5 | The 2 mm cuff band is all perimeters, with no infill seams in the part that stretches. |
| Top / bottom shell layers | stock | 5 / 5 |  |
| Sparse infill | grid 15 % | gyroid 18 % | Gyroid flexes evenly; low density turns the thick walls into light padding. |
| First-layer line width | 0.42 | 0.5 mm | Siraya's 120 % for adhesion. |
| Speeds | 200–300 (old experiment) | 20 first layer and bridges / 25 outer wall and top / 30 elsewhere | TPU needs slow, steady extrusion; 30 kept from your earlier TPU Air profile. |
| Seam | aligned | random + scarf seam | An aligned seam puts a column of weak spots up the cuff, where the hoop stretch is. |
| Avoid crossing walls | off | on | Keeps travel and its ooze inside the part. |
| Brim / skirt | brim | no brim, 1 skirt loop | The R66 cover (376 × 113 mm) only fits rotated ~45° on the 320 mm bed. |
| Supports | on (in your old files) | off | The tab sits on the bed; the taper walls lean only ~30–37°. |

## Per-part settings (live in the .3mf)
- Height-range modifier 0–5 mm: sparse infill 100 % (solid grommet tab and end-cap base).
- Layer-slider G-code for the dense/foam switches (see the Dense 240 note).

## Open recommendation
- The multicolor chat suggested switching seam to **Aligned/Back** to stop foaming blobs scattering over the outside. That trades against the cuff-strength reason above; for covers, put the aligned seam on the least-stretched side.
