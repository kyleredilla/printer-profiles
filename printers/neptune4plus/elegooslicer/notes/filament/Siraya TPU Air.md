# Siraya TPU Air (filament) — legacy

- **Parent:** `Elegoo TPU 95A @EN4 Series`
- **Status:** superseded by Siraya TPU Air - Dense 240 (and the foam switch via layer-slider G-code)
- **Origin:** your own first experiments, saved 2026-09-12 (slicer 1.3.2.9 format; also in `user_backup-v1.5.3.5`)

## Purpose
First attempt at TPU Air: printed foamed at 260 °C.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Nozzle (first / other) | stock | 260 / 260 °C | Foaming temperature |
| Flow ratio | stock | 0.6 | Close to Siraya's 55–60 % at 260 °C |
| Retraction length / speed | stock | 0 / 0 | No retraction for foaming TPU |
| Deretraction speed | stock | 30 | |
| Temperature range | stock | 230–270 °C | Siraya's range |

## Notes
- Kept in git for history. If you don't print foamed-only parts with it anymore, delete it from the slicer. Leaving the file here does no harm.
