# Public Source Census — Pokémon Y

This repository currently assumes **no local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or extracted game asset is available**. Therefore the project must reconstruct knowledge from public documentation, public source code, preserved research, official information, and independently verifiable datasets.

This file is the master census for that work. A source being listed here does **not** mean every statement in it is correct. Claims are promoted into project documentation only after source-level review and, where possible, independent cross-checking.

## Canonical regional research policy — Japanese edition as comparison origin

This project performs an **exhaustive all-region investigation with the Japanese release as the comparison origin**.

- The Japanese edition is the project's baseline coordinate for names, text, data, presentation, assets, behavior, distribution history, and version-difference tables.
- This is a research convention, **not** an assumption that the Japanese build was necessarily released earlier, is always technically older, or is internally the source build for every asset.
- Every evidenced retail region, language configuration, revision, update, demo, distribution environment, and platform-service dependency must be inventoried rather than collapsed into a generic “international version.”
- Differences are recorded directionally as `Japanese baseline → target region/language/revision`, while version-exclusive gameplay differences such as X↔Y remain a separate comparison axis.
- A localization difference is not automatically a region difference, and a region difference is not automatically a ROM/data difference. Text selection, font resources, locale flags, title/update identifiers, packaging/manual material, distribution infrastructure, and executable/data changes must be classified separately.
- Shared byte-identical or behavior-identical material should be deduplicated in the research database while preserving every region/language/revision in provenance metadata.
- Japanese official terminology and Japanese in-game text are preserved as primary comparison fields; current official Korean terminology is used for Korean-facing documentation, with historical Generation VI Korean wording separately recorded when it differs.
- No regional build, language, revision, or patch may be declared identical to another without evidence. “Same as JP” is itself a finding that requires support.
- Public-source conclusions must retain an evidence state: observed in implementation, documented by an official/contemporaneous source, independently cross-confirmed, or provisional pending stronger evidence.

### Mandatory comparison dimensions

For every data domain where public evidence exists, the census must attempt to distinguish:

1. Japanese retail/base release.
2. Other retail regions and their title/update identities.
3. Every selectable or distributed language evidenced for Generation VI.
4. Version-exclusive X versus Y behavior/data.
5. Base revision versus every downloadable update revision.
6. Demo/trial/special-distribution builds where applicable.
7. Local wireless, Internet-service, event-distribution, and peripheral/service differences by territory and time period.
8. Packaging/manual/official-web differences when they document rules, terminology, features, or content not recoverable elsewhere.
9. Censorship, rating, legal, UI, font, text-layout, naming, audio, graphical, network, or event differences tied to territory or language.
10. Later corrections or terminology changes, without retroactively rewriting what the Generation VI build actually contained.

The regional census remains open until each investigated domain has an explicit matrix of **JP baseline / target region-language / revision / evidence / difference status / unresolved gaps**.

## Evidence classes

- **A — implementation evidence:** public source code that parses, writes, validates, emulates, or edits the relevant structure.
- **B — technical documentation:** reverse-engineering notes, platform documentation, file-format documentation, or research writeups.
- **C — structured preservation data:** event archives, save/entity format corpora, machine-readable datasets, text corpora, or preserved metadata.
- **D — official / contemporaneous reference:** official game sites, manuals, patch notes, developer interviews, Nintendo / Pokémon material.
- **E — secondary cross-check:** encyclopedias, wikis, databases, guides, research forum threads, and community documentation.

A ROM-derived assertion that is only supported by E-class material remains provisional.

## Core public reverse-engineering sources

| Source | Class | Main value | Gen VI relevance | Local policy |
|---|---|---|---|---|
| `kwsch/pk3DS` | A | GARC handling; Gen VI personal data, moves, learnsets, evolutions, trainers, encounters, marts, CRO-related editing | XY + ORAS | Treat source behavior as implementation evidence; audit license before copying code |
| `TeamEXR/shutan-dev-wiki` | B | Gen VI overview; GARC, BinLinker, LZ11, scripts, sequences, text/localization, battle, field, UI notes | XY-focused with Gen VI/ORAS coverage | Verify uncertain/TODO claims elsewhere |
| `Rynbo/CTRMap` | A | Gen VI world/zone editing, collision, props, cameras, NPCs | XY + ORAS | Mine parsers/format definitions and cross-check with later forks |
| `hdent1232/CTRMap-F5` | A | Modern continuation with zone, trainer, script, geometry and collision validation; pawn script assembly/disassembly | strongest public ORAS world/script evidence; some XY support | Distinguish F5 discoveries from original assumptions |
| `gdkchan/Ohana3DS-Rebirth` | A | BCH/model/texture/animation viewing and parsing | XY + ORAS graphics | Compare with SPICA and newer importers |
| `gdkchan/SPICA` | A | H3D/BCH serialization/deserialization | XY + ORAS 3D assets | Independent implementation study |
| `sxrmss/n3ds_importer` | A | GFModel, GFMotion, GFTexture, BCH, PICA200 attributes and texture formats | explicitly covers XY/ORAS | Modern graphics cross-check; preserve tested-vs-synthetic distinction |
| `kwsch/PKHeX` | A/C | PK6/EK6, WC6, XY/ORAS save structures, legality and game-version handling | XY + ORAS | Primary public implementation source for save/entity/event formats |
| `projectpokemon/EventsGallery` + Project Pokémon Gen 6 gallery | C/E | preserved WC6/WC6FULL distributions and event metadata by language/region | XY + ORAS | Index metadata/hashes; archived cards may have incomplete restrictions |
| `abcboy101/poke-corpus` | C | standardized text dump corpus and notes on XY-style text conventions | text-format comparison | Do not republish bulk copyrighted game text; use format/metadata observations only unless permitted |

## Nintendo 3DS platform sources

- 3dbrew: NCCH/CXI/CFA, RomFS, ExeFS, filesystem services, CRO and related platform documentation.
- `3DSGuy/Project_CTR`: `ctrtool` and `makerom` implementations for NCCH/CXI/CFA/CCI/CIA, ExeFS and RomFS.
- `azahar-emu/azahar`: Citra-lineage loader, filesystem, module/CRO, GPU and service behavior.
- devkitPro `citro3d` / `tex3ds`: PICA200-facing texture formats and compression cross-checks, including LZ11 containers.

## Official and game-behavior sources to inventory

- Pokémon/Nintendo official Y/XY pages, manuals, announcements and support articles.
- Every XY update revision from 1.0 through 1.5, with official changelog wording where recoverable.
- Official localized terminology for every supported language.
- Developer interviews and contemporaneous technical/design material.
- Archived official web material when current pages no longer exist.

Secondary references such as Bulbapedia are discovery/cross-check sources, not replacements for recoverable official evidence.

## Mandatory domain sweeps

1. NCCH / ExeFS / RomFS / update-title layout.
2. ARM11 `.code`, CRO modules, relocations, executable boundaries.
3. GARC, BinLinker and compression variants.
4. Text containers, control codes, languages and fonts.
5. Event/script bytecode, native function IDs, triggers and sequences.
6. Zones, area data, geometry, collision, props, cameras, NPCs and warps.
7. Pokémon personal/form data.
8. Moves, learnsets, egg moves, evolution, TM/HM and tutors.
9. Trainers, classes, parties, AI, rewards and battle types.
10. Encounters, hordes, fishing, Friend Safari and special encounters.
11. Items, shops, berries, key items and Mega Stones.
12. Battle mechanics, type chart, abilities, weather and Mega Evolution.
13. Models, materials, textures, shaders, animations, UI and icons.
14. Audio archives, sequences, banks, streams and cries.
15. Saves, PK6/EK6, battle videos, WC6, Pokémon Link and persisted online data.
16. PSS/GTS/Wonder Trade/Battle Spot/O-Powers/Amie/Super Training.
17. X↔Y and language/region differences.
18. Patch deltas 1.0→1.5.
19. Unused/debug/inaccessible/leftover material.
20. Gen VII+ descendant implementations used only as reverse cross-checks.

## Verification rules

- Never manufacture offsets, GARC paths, command IDs, counts, hashes or asset identities.
- Record whether a fact is observed in implementation, documented, cross-confirmed, or provisional.
- Prefer two independent implementations over one wiki statement.
- XY and ORAS must remain separated where structures or behavior diverge.
- Y-specific differences must not be inferred from X without evidence.
- Patch-specific behavior must not be generalized to 1.0.
- Code copying requires license compatibility and attribution review.
- Public availability of copyrighted game data does not make it appropriate to mirror; prefer metadata, formats, hashes, tooling and independently written documentation.

## Current audit order

1. Fully index `pk3DS` Gen6 structures/config mappings.
2. Fully index Project Shutan and tag incomplete claims.
3. Diff CTRMap ↔ CTRMap-F5 Gen VI formats and script tables.
4. Index PKHeX Gen6 save/entity/mystery-gift implementations.
5. Build graphics crosswalk: Ohana3DS ↔ SPICA ↔ n3ds_importer ↔ citro3d/tex3ds.
6. Build platform crosswalk: 3dbrew ↔ Project_CTR ↔ Azahar.
7. Inventory Project Pokémon Gen VI events by language/distribution/game metadata.
8. Sweep official/archived XY material and patch/localization history.
9. Sweep secondary databases/forums after implementation/official sources are indexed.

## Status

**Open-ended exhaustive census in progress.** Completeness is tracked by explicit domain coverage and gap lists rather than assuming any single search engine, wiki or repository contains everything.