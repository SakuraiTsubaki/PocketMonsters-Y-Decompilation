# Bug / Glitch / Error Eradication — Pocket Monsters Y

Status: ACTIVE

## Goal

Remove every reproducible unintended defect from the selected Pocket Monsters Y target while preserving intentional Generation VI mechanics, data, content, version-specific behavior, and compatibility constraints.

A defect is not considered fixed until it has: (1) a documented trigger, (2) a confirmed root cause in the selected binary/data, (3) a minimal fix, and (4) a regression test proving the trigger no longer fails and intended neighboring behavior still works.

## Target gate

`config/target.json` is currently unselected. No binary-specific address, symbol, patch, or root-cause claim may be treated as confirmed until the exact release/region/revision/update and hashes are populated.

The latest official X/Y update, Ver. 1.5, is the minimum behavioral baseline. Earlier official fixes must be preserved/backported, including the Ver. 1.1 save/GTS fixes, Ver. 1.2 Wonder Trade evolution/Trainer PR fixes, and later general bug fixes.

## Initial defect inventory

### Generation VI battle logic shared with XY/ORAS
- Baton Pass + Own Tempo confusion timing
- Charge Beam additional-effect overflow under Serene Grace + pledge rainbow
- Choice-item lock persisting through item-effect suppression/removal
- threshold held items not activating immediately after confusion self-damage

### XY battle/presentation
- Battle Chateau Flabébé using Floette cry
- move-animation camera clipping
- incorrect Poké Ball send-out animation in pre-1.3 behavior

### XY systems / UI / data
- language icon stale display
- Pokémon-Amie gift state error
- Pokémon cloning transaction race/rollback exploit
- PSS save timestamp/date stale state
- reported save corruption cases (keep UNVERIFIED until reproduced and separated from SD/power-loss failure)
- stereo/surround mode mismatch
- Super Training menu trigger race
- imported Eevee -> Sylveon Pokédex registration failure
- Wonder Card form cache not refreshed
- Vivillon Friend Safari encounter icon logic (pre-1.3)
- Trainer PR Video caption progression failure (pre-1.2)
- Wonder Trade evolution move-learning loss (pre-1.2)
- GTS filter communication failure (pre-1.1)

### XY overworld / map / event
- backward sign-reading interaction
- Route 7 Day Care signpost flag/interaction inconsistency
- invisible Poké Ball interaction in Looker mission room
- Lumiose City fence collision mismatch
- Poké Radar music state corruption around Egg hatching
- Santalune Gym tent transparency/render oversight
- Sky Trainer post-battle interaction flag
- Lumiose City save/load failure (pre-1.1)

### Shared XY/ORAS UI / graphics / integration
- case-conversion table omissions for added accented characters
- graphics cache flush oversight around 3D/2D transitions
- invalid-input / stale UI text state
- Pokémon-Amie first-interaction reaction state
- Pokémon-Amie sprite freeze/state mismatch
- Pokémon Bank friendship-evolution flag bug: classify as EXTERNAL DEPENDENCY; harden client-side validation if the received state can be detected safely

## Zero-defect workflow

1. Identify exact ROM/update and record hashes in `config/target.json`.
2. Extract and hash NCSD/NCCH, ExeFS, RomFS, code, CRO/modules, archives, scripts, maps, text, graphics, audio, and save-related structures.
3. Reproduce every known defect on the selected baseline and record unaffected/affected revisions.
4. Diff base game against every official update to recover Nintendo/Game Freak fixes before inventing replacements.
5. Audit adjacent code paths for same root-cause families: bounds, stale cache/state, bad flags, missing transaction rollback, race/order bugs, invalid enum/index handling, collision/render mismatch, text/data table omissions.
6. Patch the smallest root cause, not the symptom.
7. Add automated regression tests or deterministic replay/state tests for every fixed defect.
8. Fuzz parsers, save/state transitions, battle state machines, UI menus, script inputs, malformed/edge Pokémon data, map transitions, and communication serialization.
9. Run full story/event/battle/network-offline compatibility regression suites.
10. Mark FIXED only after clean-room reproduction fails on the patched build and all regression checks pass.

## Severity classes

- S0: data loss / save corruption / security / arbitrary invalid-state acceptance
- S1: crash / freeze / softlock / progression blocker
- S2: battle-rule or game-state corruption / duplication / transaction failure
- S3: incorrect data, event, map, UI, audio, graphics, or animation behavior
- S4: cosmetic-only defect with no persistent state impact

## Sources used to seed this inventory

- Nintendo Support — How to Update Pokémon X and Pokémon Y
- Bulbapedia — List of glitches in Generation VI
- Bulbapedia — List of battle glitches in Generation VI
- Bulbapedia — List of overworld glitches in Generation VI

These sources are leads, not binary proof. The selected ROM/update is authoritative for final reproduction and fixes.
