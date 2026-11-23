# Siraya TPU Air - Surface 230 (filament)

- **Parent:** Dense 240 / Logo presets
- **Status:** testing
- **Used by:** splice_inlay v4: logo + body surface layers up to the logo top
- **Origin:** [Multicolor TPU logo printing](https://claude.ai/chat/a6701a89-15db-4018-8db1-fb87bd4eb8a4)
- **Location found:** Mac: `~/base/print_splicing/R22_stab_cover/profiles/`

## Purpose
Low-foam preset for the visible bottom face and the inlaid logo. It foams less at 230 °C, so retraction actually works and the surface is denser. splice_inlay v4 switches to Dense 240 (the foaming body) above the logo top.

## Settings changed (vs. parent)

| Setting | Parent / before | Value | Why |
|---|---|---|---|
| Nozzle temp | 240 | 230 °C | Bottom of Siraya's 230–270 °C range: denser, stiffer (~85A), least foaming, less ooze. |
| Flow ratio | 0.53 | **0.72** (created as 0.60) | Created as a guess (~13 % over the 240 °C value, since it foams less). Set from ElegooSlicer **Flow rate calibration Pass 1** (9 blocks, modifiers −20…+20) run at 230 °C from 0.60: 0.60 × (100 + 20) / 100 = 0.72, so the **+20 block** won (you recalled "about +10", which would give 0.66). +20 is the edge of the range and Pass 2 wasn't run, so the true value may be higher; see To verify. |
| Retraction / speed / deretraction | 0 | 0.8 mm / 25 / 15 mm/s | Same reasoning as the Logo preset. |
| Wipe | off | 1.5 mm |  |
| Z-hop | 0 | 0.2 mm |  |

## Rules
- The logo and `body_surface` slices must both use this preset: same temperature for colour/texture match and for the splicer reheat (the script warns if they differ).
- If you change the temperature, rename the preset to match and recalibrate flow.

## Test results so far
- Temperature tower 235→215 °C: stringing and bumps looked the same at every temperature; colour darkened toward 215 (less foam).
- Likely causes, in order: wet filament, random seam scattering blobs, flow too high.
- Recommended: dry at 70–80 °C for 4–6 h, set seam to Aligned/Back, run Orca's two-pass flow calibration (Pass 1 then Pass 2: flow × (100 + modifier) / 100). Then pick the coolest band that bonds as well as 235 °C.

## To verify
- Re-run **Pass 1 with the preset at 0.72**. If 0 wins, run Pass 2 (−9…0) to fine-tune. If +5 or higher wins, the best value is above the first grid's range; apply the formula again and repeat.
- Calibrate on dried filament (70–80 °C, 4–6 h). Moisture increases foaming and shifts the flow you need.
