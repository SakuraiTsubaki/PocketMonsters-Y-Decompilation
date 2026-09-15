# Decompilation Start

This document marks the transition from repository setup into active Pokémon Y decompilation work.

## Operating rule

The retail game image is a local, read-only source. ROM/game-image binaries, decrypted title keys, console keys, and other sensitive key material are not committed to this repository. Reconstructed source, analysis, manifests, tooling, tests, metadata, and independently reproducible findings belong in Git.

## Phase 0 — Target identity

Before interpreting offsets or structures, every observation must be tied to an exact local target.

1. Preserve the original local target unchanged.
2. Record file size and SHA-256 with `tools/target_inventory.py`.
3. If an extracted working tree is used, inventory that tree separately.
4. Record region/language/revision/update information only when directly verified.
5. Never copy game-image bytes into a manifest.

## Phase 1 — Container and executable map

For a verified local Nintendo 3DS target, document the hierarchy before decompiling code:

- outer game-image/container identity
- partitions/content units actually present in the verified target
- executable filesystem (ExeFS) inventory
- read-only filesystem (RomFS) inventory
- executable/code image identity and section mapping
- resource archives and compression layers encountered in the target

Do not assume that a layout from Pokémon X, Omega Ruby, Alpha Sapphire, or another 3DS title is identical.

## Phase 2 — Executable reconstruction

Proceed from observed binary evidence: establish load/section boundaries, record provisional function identifiers and cross-references, separate runtime/library patterns from game-specific code, rename symbols only with evidence, and preserve provenance back to observed binary ranges.

## Phase 3 — Game-data reconstruction

Track executable and resource work independently. Candidate categories include GARC and other containers, scripts/events, Pokémon/battle/system parameters, maps/field data, models/textures/animations/UI, text/message resources and language variants, and audio metadata/resource indices.

## Generation VI comparison rule

Pokémon Y is reconstructed as its own verified target first. Cross-title comparison uses three explicit buckets:

- **XY common** — independently verified in both X and Y
- **Generation VI common** — independently verified across the relevant XY and ORAS targets
- **title/version specific** — observed only in one title, region, revision, language, or update state

## Current state

- Repository baseline: established
- ROM exclusion policy: established
- Target identity tool: added
- Target identity tests: added
- Verified Pokémon Y retail target manifest: pending a locally available source
- ExeFS/RomFS map: pending a locally available source
- Executable source reconstruction: not yet started
