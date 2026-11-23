# FS PET GF 0.2 mm - vacuum adapter (print profile)

- **Copied from:** your own copy "FS PET GF 0.2 mm" (itself copied from the built-in PET GF template `ac1002e4…`)
- **Status:** active
- **Origin:** [Vacuum hose adapter design](https://claude.ai/chat/84a5679a-ee14-4c19-96aa-f3e2d681614c)

## Purpose
A solid, accurate-fit vacuum hose adapter in PET-GF15, plastic only (Speedy block edited).

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| InsetXPCount (inner walls) | 1 | 6 | Inset0 = 2 outer walls; 2 + 6 = 8 walls, which fills the part solid. |
| Inset0Speed (outer) | 200 | 80 mm/s | Round, accurate mating surfaces. |
| InsetXPSpeed (inner) | 250 | 120 mm/s | Better bonding between all those walls. |
| GenerateBrim / BrimLoops | off / 2 | on / 12 | ~5 mm, outer edge only: narrow contact ring on a 3.5" tall part. |
| InfillSBottomLayerCount | 3 | 5 | ~1 mm solid base. |
| (material link) | — | `PlasticId 05530460…` | Your PET GF material; not in this repo yet (export it to add it). |

## Set in the PET-GF material, not here
- Nozzle 290 °C (295 °C first layer; manual range 280–310), bed 75 °C, fan off, retraction ~1 mm.
- Dry at 65–70 °C for 8 h. Use a hardened plastic nozzle: glass fiber wears brass quickly.

## To verify
- **Resolved:** the edit kept ProfileGroup Id `49a3a6b3…`, which belongs to *your copy* "FS PET GF 0.2 mm", not the built-in template (built-ins can't be edited). So the import renamed and changed your copy, and the stock template is untouched. Make a fresh copy from the built-in if you want a plain PET GF 0.2 mm again.
- Seam wasn't changed: the file stores it as a number of unknown meaning. Set aligned or rear in the slicer.
- Stock `BottomSkinEWMM` is 0.01 (same apparent typo as the TPU profile); left alone here.
- Fit adjustments without CAD changes: `HolesExpansion` and `OuterContourExpansion`. Prefer editing the model, because outer-contour changes also move the socket's outside diameter.
