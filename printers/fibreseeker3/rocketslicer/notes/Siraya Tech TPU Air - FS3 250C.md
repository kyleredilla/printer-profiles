# Siraya Tech TPU Air - FS3 250C (plastic material)

- **Copied from:** stock PETG plastic template
- **Status:** active
- **Origin:** [Fiberseeker TPU profile setup](https://claude.ai/chat/4eea174a-e2b5-4b56-9399-7a021f574900) (replaced the first version from [TPU Air filament setup](https://claude.ai/chat/63882b13-8f59-4af6-aecd-04838b89ac69))

## Purpose
TPU Air on the FibreSeeker 3's right plastic nozzle, FFF only (Speedy). It can't be used with continuous fiber, and the composite nozzle isn't usable for plastic on its own.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| TemperaturePrint / OnFLs | 250 | 250 °C | Middle of Siraya's range; 240 °C at flow ~0.65–0.70 gives crisper detail (v1 used 260). |
| ExtrusionMultiplierP (flow) | 1.00 | 0.60 | Foams at this temperature. Guide: 240 °C ≈ 0.65–0.70, 260 ≈ 0.55, 270 ≈ 0.50. |
| BedTemperature / OnFLs | 75 | 40 °C | Siraya 30–45 °C; PVP glue on PEI. |
| RetractionSpeed / LengthOnTravel | 20 / 1 | 0 / 0 | Siraya: retraction off for foaming TPU. |
| RetractionLengthOnToolChange / ExtraLengthPOnToolChange | 5 / — | 0 / 0 | Pulling soft TPU back 5 mm risks a jam. |
| ZHopP | 0.4 | 0 | No retraction, so a hop only adds strings. |
| RegularFanSpeed / MaximumFanSpeed | 20 / 80 | 100 / 100 | Siraya: 100 %. The first layer still runs fan-off. |
| MaxVolumetricSpeed | 25 | 8 mm³/s | Soft TPU feed limit (v1 used 4; raised in the review). |
| Density / CostPerSpool | 1.27 / 20 | 1.2 / 49.99 | Estimates only. |

## Left alone on purpose
- `PlasticType` stays "PETG" and `Manufacturer` stays "FIBRESEEK": the slicer may reject other values on import.
- Internal `Id` kept, so re-importing overwrites this entry instead of duplicating it. The print profile links to it by that Id.

## Handling
- Dry at 70–80 °C for 4–6 h in a filament dryer (a household oven won't hold that accurately). Wet TPU Air pops, bubbles and foams unevenly.
