# Elegoo PLA+ @EN4 - Overhang Cool 60 (filament)

- **Parent:** `Elegoo PLA+ @EN4 Series`
- **Status:** active (job-specific)
- **Used by:** dart box Rev B base: the back plate printed over supports
- **Origin:** [Dart box rework in Fusion 360](https://claude.ai/chat/d8768692-00b6-4a82-bbe1-549cfc11935a) (2026-11-23)

## Purpose
Stock PLA+ with gentler cooling on overhangs, bridges and support interfaces, so the first plate layers printed over support don't curl at the corner.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Overhang and external bridge fan | 100 % | 60 % | The first plate layers over support print as bridges; full fan curls them |
| Support interface fan | (normal fan) | 60 % | Top layers of the support |
| Internal bridge fan | (overhang fan) | 60 % | Bridges inside the part |
| Force cooling for overhangs and bridges | on | on | Makes the 60 % values actually apply |
| No cooling for the first N layers | 1 | 3 | Keeps the first layers warm so they don't lift |
| Full fan speed at layer | 0 | 6 | Ramps the fan up instead of jumping to 100 % |

## Notes
- Everything else is stock: 220 °C nozzle, 60 °C bed, 0.98 flow, 100 % fan for normal printing.
- It works for both PLA+ and Rapid PLA+ (Elegoo's two profiles are nearly identical).
- Every overhang and bridge in a part prints at 60 % with this preset. Use your normal PLA+ preset for other parts.
- It was delivered as a full 62-key profile; the slicer kept only the 6 changed keys on save. That's expected.
