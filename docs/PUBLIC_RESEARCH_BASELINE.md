# Public Research Baseline — ROM-less Phase

Last reviewed: 2026-09-14

## Current constraint

No local Pokémon Y ROM, cartridge dump, CIA/CCI, extracted RomFS, or extracted ExeFS is currently available to this project.

Accordingly, this repository must distinguish **publicly documented/reconstructed knowledge** from **facts verified directly against a Pokémon Y dump**. Until a lawful source dump is available, exact hashes, offsets, archive contents, per-revision binary layouts, and rebuild equivalence remain unverified.

## High-value public research sources

### pk3DS
- Repository: https://github.com/kwsch/pk3DS
- Scope: 3DS Pokémon ROM editor/randomizer with source code for XY/ORAS and later 3DS titles.
- Useful research areas include trainer battles, wild encounters, personal/species data, move data, level-up and egg learnsets, evolutions, TM data, and shop inventories.
- Policy: treat implementations as research references; review license/attribution before reusing code.

### Project Shutan developer wiki
- Repository: https://github.com/TeamEXR/shutan-dev-wiki
- Scope: Generation VI reverse-engineering notes and 3DS architecture documentation.
- Documented areas include GARC archives, Binary Linked archives, LZ11 compression, scripts, sequences, text/localization, graphics assets, field systems, battle systems, and UI.
- Pokémon XY documentation is directly relevant, but every statement should still be independently verified when source files become available.

### Project_CTR / ctrtool / makerom
- Repository: https://github.com/3DSGuy/Project_CTR
- Scope: Nintendo 3DS container tooling.
- `ctrtool` documents/extracts formats including ExeFS, RomFS, NCCH/CXI/CFA, CIA, NCSD/CCI, exheader, TMD, tickets, and related structures.
- `makerom` provides reconstruction tooling for CTR containers.

### PKHeX
- Repository: https://github.com/kwsch/PKHeX
- Scope: Pokémon save/entity format implementations, including Generation VI data structures.
- Useful for PK6/entity layouts, save substructures, Mystery Gift structures, checksums, and game-data semantics that are independent of the retail executable decompilation.

### CTRMap-F5
- Repository: https://github.com/hdent1232/CTRMap-F5
- Scope: current Generation VI world editor/research implementation for X/Y and ORAS.
- Useful as a research reference for maps, zones, events, scripts, trainers, shops, models, textures, collision, and world-data relationships.
- The project is GPL-3.0 and explicitly does not ship retail game data; license boundaries must be respected.

### Nintendo 3DS graphics research
- Ohana3DS-Rebirth: https://github.com/gdkchan/Ohana3DS-Rebirth
- n3ds_importer: https://github.com/sxrmss/n3ds_importer
- Useful format families include BCH/H3D, GFModel, GFMotion, GFTexture, PICA200 vertex data, materials, textures, skeletons, and animations.

## Work that can proceed without a ROM

- Maintain a cited source inventory and provenance ledger.
- Document known 3DS container and Generation VI archive formats.
- Design independent parsers/writers from published format specifications.
- Create synthetic fixtures and round-trip tests that contain no retail game data.
- Define schemas for species, moves, encounters, trainers, scripts, text, maps, models, and save structures.
- Build repository scaffolding, tooling interfaces, manifests, validators, and research notes.
- Compare public implementations and record disagreements or unknown fields.
- Track license and attribution requirements for every external implementation consulted.

## Work blocked until a source dump exists

- Pokémon Y file-by-file RomFS/ExeFS inventory verified from the retail title.
- Exact archive paths and contents verified against a specific revision/region.
- Executable symbol/function recovery tied to retail `.code` or CRO modules.
- Retail graphics/audio/text extraction.
- Exact offsets, hashes, signatures, and binary-diff validation.
- Bit-identical or functionally equivalent rebuild verification against the original title.

## Verification rule

Third-party path maps, offsets, labels, and inferred structures are **research leads**, not canonical facts. They may be entered into notes with provenance, but they become project-verified only after independent confirmation against an identified game version/revision or multiple sufficiently independent primary/technical sources.

No ROM images or redistributed retail binaries are to be committed to this repository.
