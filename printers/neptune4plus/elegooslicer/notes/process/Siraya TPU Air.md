# Siraya TPU Air (process) — legacy

- **Parent:** `0.20mm Standard @Elegoo N4Plus 0.4 nozzle`
- **Status:** superseded by Siraya TPU Air - Stab Cover
- **Origin:** your own first experiments, saved 2026-09-12 (slicer 1.3.2.9 format; also in `user_backup-v1.5.3.5`)

## Purpose
First TPU Air process: Standard slowed to TPU speeds.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| First layer / first-layer infill | stock | 20 / 20 mm/s | TPU |
| Outer / inner wall, small perimeters | stock | 30 / 30 / 30 mm/s | TPU |
| Sparse / internal solid infill, top surface | stock | 30 / 30 / 30 mm/s | TPU |
| Supports | off | on | |

## Notes
- Stab Cover keeps these speeds (25 on outer wall and top) and adds the cuff and padding settings. It turns supports off.
- Safe to delete from the slicer; the history stays in git.
