# Siraya Tech TPU Air 0.2 mm (FS3) — print profile, file `Siraya_Tech_TPU_Air_0.2_mm_FS3.json`

- **Copied from:** stock PETG 0.2 mm profile
- **Material link:** `PlasticId` → TPU Air - FS3 250C (`6abd5ab5…`; stock PETG was `861c455e…`)
- **Status:** active
- **Origin:** [TPU Air filament setup](https://claude.ai/chat/63882b13-8f59-4af6-aecd-04838b89ac69) → [Fiberseeker TPU profile setup](https://claude.ai/chat/4eea174a-e2b5-4b56-9399-7a021f574900)

## Purpose
Only the **Speedy** (plastic-only) block is enabled and edited; the ReinForced and Fortified blocks are untouched placeholders.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| First layer speed / width | 50 / 0.40 | 20 mm/s / 0.48 mm | 120 % width for adhesion. |
| Outer / inner walls | 200 / 300 | 30 / 40 |  |
| Infill | 300 | 40 |  |
| Top surface / layers under it | 100 / 100 | 30 / 35 |  |
| Bottom-most / other bottom | 50 / 50 | 20 / 30 |  |
| Gap fill / small infill | 30 / 100 | 20 / 30 |  |
| Bridges / overhangs | 50–150 | 20–25 |  |
| Supports / interface | 150 / 100 | 30 / 25 |  |
| Z-hop, DoRetractOnLayerChange, coasting | on | off | Retraction is also off in the material; this profile has its own layer-change switch. |
| Avoid crossing perimeters | — | on | Keeps travel and ooze inside the part. |
| BottomSkinEWMM | 0.01 | 0.4 | Looked like a typo (ReinForced has 0.4); could starve bottom layers if used. |
| InfillPCellularExtrusionMultP | 1.10 | 1.00 | Multiplies with the material's 0.60; the extra 10 % over-packed the infill and pushed foam into the top layers. First layer stays 1.10, skirt 1.20 (primes, since there's no retraction). |
| StartGcode / EndGCode | — | `MOTION_FILAMENT_SENSOR ENABLE=0` / `ENABLE=1` | Klippy logs: the clog sensor `filament_sensor_4` on extruder1 trips after 7 mm with no pulse (the firmware resets the configured 12 mm to 7 at boot). TPU fed at ~0.65 mm/s slips past the wheel → false "clogging" pauses. |

## Caveats
- If you cancel a TPU print, the end G-code doesn't run: run `MOTION_FILAMENT_SENSOR ENABLE=1` or reboot before printing PETG or fiber.
- With the sensor off, a real jam won't pause the print. Check the drive gear on long jobs.
- Pressure advance (the `SET_PRESSURE_ADVANCE ... ADVANCE=` line in the start G-code) is still the PETG value 0.06. Tune it if corners bulge or line starts are thin.
- Prime tower is off (correct for a single nozzle).
