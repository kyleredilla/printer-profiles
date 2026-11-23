# Siraya TPU Air - Stab Cover Surface (process)

- **Parent:** Stab Cover (copied values)
- **Status:** testing
- **Used by:** splice_inlay v4: logo slice and `body_surface` slice
- **Origin:** [Multicolor TPU logo printing](https://claude.ai/chat/a6701a89-15db-4018-8db1-fb87bd4eb8a4)
- **Location found:** Mac: `~/base/print_splicing/R22_stab_cover/profiles/`

## Purpose
Stab Cover settings for the surface/logo slices that get spliced together.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Travel speed | stock | 200 mm/s | Less time for ooze to string out across the logo. |
| Skirt loops | 1 | 0 | The spliced file already primes on the body slice; a skirt would print twice. |
| Speeds / accel (copied) | — | first layer 20, outer 25, inner and infill 30, bridges 20; accel 5000 default / 2500 outer / 2000 top / 500 first layer | Same as Stab Cover. |
| Arc fitting | — | on |  |

## Rule
- Layer height and first-layer height **must match** Stab Cover, or the two cover slices won't line up (the splicer warns).
