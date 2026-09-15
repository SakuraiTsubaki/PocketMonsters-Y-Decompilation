# Phase 1 — Container and Filesystem Map

Generation VI decompilation proceeds across Pokémon X, Pokémon Y, Pokémon Omega Ruby, and Pokémon Alpha Sapphire in parallel.

## Required evidence

A Phase 1 record must come from a verified local target and must identify the exact region, language, revision/update state, and SHA-256 before structural conclusions are promoted.

## Inventory order

1. Record the untouched local game image with `tools/target_inventory.py`.
2. Inventory the extracted working tree separately.
3. Record ExeFS and RomFS contents by relative path, size, and SHA-256.
4. Compare paired titles with `tools/compare_manifests.py`.
5. Promote a structure to a shared bucket only after direct confirmation in every required title.

## Comparison buckets

- **X-specific / Y-specific** — observed in only one XY title.
- **XY common** — independently matched in X and Y.
- **Omega Ruby-specific / Alpha Sapphire-specific** — observed in only one ORAS title.
- **ORAS common** — independently matched in Omega Ruby and Alpha Sapphire.
- **Generation VI common** — independently matched across the relevant XY and ORAS targets.
- **region/language/revision/update specific** — never merged into a title-common bucket without evidence.

## First outputs

For each verified target, preserve only metadata and reconstructed analysis in Git: source identity manifest, extracted-tree identity manifest, ExeFS/RomFS file lists and hashes, pairwise comparison reports, and notes identifying unchanged/changed/added/removed paths.

Game images, decrypted key material, and private console keys remain local and are never committed.
