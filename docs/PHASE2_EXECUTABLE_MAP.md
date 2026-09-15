# Phase 2 — Extracted Tree and Executable Map

This phase is performed in parallel for Pokémon X, Pokémon Y, Pokémon Omega Ruby, and Pokémon Alpha Sapphire.

## Generic Nintendo 3DS facts used as the platform baseline

The public CTR/NCCH documentation describes an executable NCCH/CXI as containing an extended header plus optional ExeFS and RomFS regions. ExeFS commonly contains `.code`, `icon`, `banner`, and `logo`; the ExHeader System Control Info records the text, read-only, and data CodeSetInfo fields and a flag indicating whether the ExeFS code is compressed.

These are platform facts only. They do **not** establish Pokémon-specific paths, offsets, compiler identities, functions, symbols, or resource meanings.

## Repository tools

- `tools/extracted_tree_map.py` inventories an already-extracted local target using relative paths, sizes, SHA-256, structural layer, and conservative role labels.
- `tools/exheader_codeset.py` parses only the documented System Control Info / CodeSetInfo fields from a locally supplied ExHeader.
- `tools/compare_manifests.py` compares title manifests path-by-path.

## Required sequence for every title

1. Verify the untouched local source identity.
2. Inventory the extracted tree.
3. Identify the ExHeader, ExeFS, and RomFS actually present.
4. Parse ExHeader CodeSetInfo without assigning Pokémon-specific semantics.
5. Identify the executable code file actually present in ExeFS.
6. Record hashes and sizes for all layers.
7. Compare X↔Y and Omega Ruby↔Alpha Sapphire before promoting common structures.
8. Compare verified XY-common structures against verified ORAS-common structures before calling anything Generation VI common.

## Evidence buckets

Every finding must remain in one of these states until promoted by direct evidence:

- title specific
- XY common
- ORAS common
- Generation VI common
- region/language/revision/update specific

## What does not enter Git

Retail game images, decrypted title/console keys, and private console material remain local. Metadata, hashes, independently authored tooling, analysis, tests, manifests, reconstructed source, and verification records may be committed.
