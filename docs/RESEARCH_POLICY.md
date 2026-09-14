# Research Policy — Pokémon Y

This repository is operated under three fixed principles.

## 1. No local ROM baseline

The project assumes no local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or extracted retail asset is available. Research must therefore proceed from public source code, official material, public reverse-engineering documentation, preserved datasets, historical archives, public tools, and independently verifiable secondary references.

No claim may be presented as directly retail-ROM verified unless such verification actually becomes possible later.

## 2. Japan-first, all-region census

The Japanese release is the comparison origin for this repository. Every discovered regional, language, revision, patch, distribution, and service-era difference is recorded relative to the Japanese baseline whenever possible.

The comparison axes are kept separate:

- game/version
- region
- language
- revision
- update/patch version
- distribution or service state
- date/time context when relevant

"Japan-first" is a research-coordinate rule. It does not by itself assert development ancestry, build precedence, or earlier release unless independently supported.

All confirmed region/language combinations must be investigated. "Overseas version" or "English version" must not be used as a substitute for region-specific and language-specific records when finer evidence exists.

## 3. GitHub is the project record

All project-produced research results must be committed to this repository rather than existing only in chat, local scratch notes, or undocumented external state.

This includes, as applicable:

- source inventories and provenance records
- research notes and source reviews
- comparison tables and region/language matrices
- version/revision/patch matrices
- format documentation
- independently written parsers, converters, validators, and analysis scripts
- tests and synthetic fixtures
- structured reconstructed data
- manifests, hashes, indexes, and gap lists
- verification status and contradiction logs
- maps of public implementation evidence
- documentation of unresolved questions
- human-viewable previews produced by the project when appropriate

Retail ROM/CCI/CIA binaries and other excluded proprietary binaries are not committed. Public availability of copyrighted game content does not automatically make mirroring appropriate; prefer original documentation, independently written tooling, metadata, hashes, indexes, structural descriptions, and legally compatible source material.

## Required evidence states

Every nontrivial claim should be classifiable as one of:

- official
- implementation-observed
- documented
- independently cross-confirmed
- provisional
- conflicting
- unverified

The repository must preserve source provenance closely enough that a later researcher can retrace why a conclusion was accepted.

## Deduplication and regional storage rule

Do not duplicate identical material merely because it applies to multiple regions or languages. Store a canonical record once where practical and record applicability/provenance in manifests. Store region-specific material as deltas from the Japanese baseline when that representation is accurate and lossless.

## Completeness rule

"Exhaustive" is tracked through explicit coverage matrices and gap lists. A domain is not complete merely because one wiki, repository, search engine, or archive was searched. Each major Generation VI domain must be swept across official, implementation, technical-documentation, preservation, historical, and secondary-reference sources as applicable.

This policy is mandatory for all future work in this repository.