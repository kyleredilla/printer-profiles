# Siraya TPU Air - Dense 240 Logo (filament)

- **Parent:** `Elegoo TPU 95A @EN4 Series` (copy of Dense 240)
- **Status:** testing
- **Used by:** logo slice only, for splice_inlay inlays
- **Origin:** [R22 horizontal stabilizer cover](https://claude.ai/chat/66a8d21c-e0f8-4cdc-9447-bed9be27920d)

## Purpose
Dense 240 with retraction, wipe and Z-hop added, to stop stringing and blobs on the many short travel moves between logo letters. Use it **only** for the logo slice; the body keeps Dense 240 so both print at 240 °C and the splicer's reheat stays correct.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Flow ratio | 0.53 | 0.50 | ~6 % under the calibrated value to lower nozzle pressure, which drives ooze on travel moves. Back to 0.53 if letters show gaps or a rough top. |
| Retraction length / speed | 0 / 0 | 0.8 mm / 25 mm/s | Pulls pressure off the nozzle before a travel move. |
| Deretraction speed | 30 | 15 mm/s | Slower un-retract so the soft filament doesn't buckle in the extruder. |
| Wipe / distance | off | on / 1.5 mm | Wipes the nozzle along the path before travelling. |
| Retract before wipe | — | 70 % | Most of the retraction happens before the wipe, the rest during it. |
| Z-hop | 0 | 0.2 mm | Lifts over letters already printed instead of dragging across them. |

## Pair with (process, logo slice)
- Avoid crossing walls on; travel speed ~200 mm/s.

## Troubleshooting
- Extruder grinding or skipping: drop retraction to 0.5 mm.
- Still stringing: try 1.2 mm.

## To verify
- Inherits the `filament_density` 0.88 typo from Dense 240.
- Surface 230 targets the same job (logo + surface layers) at a lower temperature. Once one of the two is proven, mark the other superseded.
