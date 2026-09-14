# pk3DS Index 01 — Generation VI core data structures

## Scope and evidence state

This is the first source-level index of `kwsch/pk3DS` for Generation VI. It records what the public implementation does; it is **not** direct observation of this repository's retail Pokémon Y target because no local retail image is available.

Pinned upstream revision reviewed:

- repository: `kwsch/pk3DS`
- branch: `master`
- commit: `6daaca934ca2284a73ab743bf89c848c57cd9de1`
- commit date: `2026-02-27`

Evidence class: **A — public implementation evidence**.

Any path, count, offset, or semantic name below must remain implementation-backed/reference evidence until independently cross-checked or later verified against a lawful target.

## 1. Game selection and high-level initialization

Source: `pk3DS.Core/Game/GameConfig.cs`

pk3DS currently distinguishes its extracted game layouts with file-count constants:

| pk3DS game family | file count used by `GameConfig` |
| --- | ---: |
| XY | 271 |
| ORAS demo | 301 |
| ORAS | 299 |

This is a pk3DS classification heuristic, **not a retail ROM fingerprint** and not evidence that every regional/revision build has an identical unpacked-file count.

For Generation VI, `GameConfig` initializes personal data, level-up learnsets, game text, move data, evolution data, and game information. It reports GARC version 4 for both XY and ORAS.

### Important XY / ORAS move-container difference

- XY: each file in the `move` GARC is parsed directly as a `Move6` record.
- ORAS: file 0 of the `move` GARC is additionally unpacked as a `Mini` container named/magicked `WD`, and its contained files are parsed as `Move6` records.

Do not apply the ORAS move-container layout to Pokémon Y without evidence.

## 2. pk3DS logical GARC map

Source: `pk3DS.Core/Game/GARCReference.cs`

`GARCReference` converts a three-digit logical file number into `a/<hundreds>/<tens>/<ones>`. These are pk3DS mappings, not retail-verified mappings in this project.

### XY mapping used by pk3DS

| logical name | number | pk3DS path |
| --- | ---: | --- |
| `encdata` | 012 | `a/0/1/2` |
| `trdata` | 038 | `a/0/3/8` |
| `trclass` | 039 | `a/0/3/9` |
| `trpoke` | 040 | `a/0/4/0` |
| `move` | 212 | `a/2/1/2` |
| `eggmove` | 213 | `a/2/1/3` |
| `levelup` | 214 | `a/2/1/4` |
| `evolution` | 215 | `a/2/1/5` |
| `megaevo` | 216 | `a/2/1/6` |
| `personal` | 218 | `a/2/1/8` |
| `item` | 220 | `a/2/2/0` |
| `gametext` | 072 | `a/0/7/2` + language-relative offset |
| `storytext` | 080 | `a/0/8/0` + language-relative offset |

### ORAS mapping retained for comparison

| logical name | number | pk3DS path |
| --- | ---: | --- |
| `encdata` | 013 | `a/0/1/3` |
| `trdata` | 036 | `a/0/3/6` |
| `trclass` | 037 | `a/0/3/7` |
| `trpoke` | 038 | `a/0/3/8` |
| `move` | 189 | `a/1/8/9` |
| `eggmove` | 190 | `a/1/9/0` |
| `levelup` | 191 | `a/1/9/1` |
| `evolution` | 192 | `a/1/9/2` |
| `megaevo` | 193 | `a/1/9/3` |
| `personal` | 195 | `a/1/9/5` |
| `item` | 197 | `a/1/9/7` |
| `gametext` | 071 | `a/0/7/1` + language-relative offset |
| `storytext` | 079 | `a/0/7/9` + language-relative offset |

### Language-relative paths

pk3DS marks `gametext` and `storytext` as `LanguageVariant` and applies the selected language integer as a relative GARC-number offset. Exact retail language-index semantics and cross-market identity remain to be independently audited.

## 3. Pokémon personal data

Sources: `PersonalInfoXY.cs`, `PersonalInfoORAS.cs`, `PersonalTable.cs`.

| format | record size |
| --- | ---: |
| XY | `0x40` bytes |
| ORAS | `0x50` bytes |

XY fields exposed by pk3DS include six base stats, two types, catch rate, evolution-stage field, packed EV yield, three held-item slots, gender, hatch cycles, base friendship, EXP growth, two egg groups, three abilities, escape rate, form stats index, form sprite/count, color/sprite bits, base EXP, height, weight, TM/HM compatibility, and type-tutor compatibility. `0x3C..0x3F` is explicitly left unknown by pk3DS.

ORAS inherits the XY model and adds four `0x04`-byte `SpecialTutors` bitfield groups at `0x40`, `0x44`, `0x48`, and `0x4C`.

## 4. Move data

Source: `pk3DS.Core/Structures/Moves/Move6.cs`.

pk3DS models a Generation VI move record as `0x22` bytes. Exposed fields include type, quality, category, power, accuracy, PP, priority, hit range, inflicted-effect data, effect probability/duration, turn range, critical stage, flinch, effect-sequence ID, recoil, healing, target, three stat effects with stages/probabilities, and a 32-bit `MoveFlag6` field.

## 5. Level-up learnsets

Source: `pk3DS.Core/Structures/Learnset.cs`.

`Learnset6` treats each ordinary entry as a signed 16-bit move ID plus signed 16-bit level and writes a 32-bit `-1` terminator. XY and ORAS both use `Learnset6`, despite using different GARC path numbers.

## 6. Evolution data

Source: `pk3DS.Core/Structures/Gen6/Evolutions.cs`.

`EvolutionSet6` is eight 6-byte slots (`0x30` bytes total). Each slot contains three little-endian 16-bit fields: method, method-dependent argument, resulting species.

## 7. Trainer data

Source: `pk3DS.Core/Structures/Gen6/TrainerData6.cs`.

pk3DS explicitly branches XY and ORAS trainer headers:

- XY `Format` and `Class`: 8-bit each.
- ORAS `Format` and `Class`: 16-bit each, followed by another 16-bit field.

Shared fields include battle type, party count, four items, AI, unknown bytes, healer flag, money, and prize. Party records include IV byte, packed configuration/PID byte, level, species, form, optional held item, and optional four move IDs.

This means Pokémon Y trainer structure must not be silently replaced by the ORAS header definition.

## 8. Encounter handling — first index only

pk3DS uses separate Generation VI wild editors:

- `Gen6/XYWE.cs`
- `Gen6/RSWE.cs`

The ORAS editor contains commentary distinguishing its encounter layout from the older XY layout. A dedicated encounter-format audit is required before canonicalizing slot layouts.

## 9. Mega Evolution audit lead

`Gen6/MegaEvoEditor6.cs` contains an ORAS-specific branch for Rayquaza entry 384 and describes its Dragon Ascent activation exception. Keep this as a later ORAS comparison lead; it does not define Pokémon Y's retail battle engine.

## Confidence / verification status

| Finding | Current project state |
| --- | --- |
| listed pk3DS files/classes | Reviewed at pinned upstream commit |
| XY/ORAS branch behavior | Public implementation evidence |
| record sizes/offsets | Public implementation evidence |
| logical GARC purpose/path map | Public implementation evidence; retail verification pending |
| exact X↔Y equality for each structure | Not yet established by this source alone |
| regional/revision equality | Unknown |
| retail hashes / byte matches | Unavailable |

## Next pk3DS batch

Audit XY/ORAS encounter tables, egg moves, Mega Evolution tables, item data, Maison data, text references/language indices, and ExeFS/CRO mappings. Cross-check each subsystem with another implementation before promoting semantics to project-canonical status.
