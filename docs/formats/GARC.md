# Generation VI GARC — Research Note

Status: **public-source reconstruction; retail Pokémon Y dump not yet available for direct verification**

Last reviewed: 2026-09-14

## Purpose

GARC is the principal Game Freak archive family used by Generation VI Pokémon RomFS data. This note records only the structure that can currently be supported by public reverse-engineering sources. It deliberately separates confirmed agreement between implementations from claims that still require validation against a retail dump.

## Public sources compared

1. Project Shutan developer wiki — `GameFreak Archives (GARCs).md`
   - https://github.com/TeamEXR/shutan-dev-wiki
2. pk3DS — `pk3DS.Core/CTR/GARC.cs`
   - https://github.com/kwsch/pk3DS

No source code from those projects is copied here; this file is an independent structural summary and provenance record.

## High-confidence common structure

Public implementations agree on four logical sections:

1. Main GARC header
2. FATO — file-allocation-table offsets
3. FATB — entry bit-vector plus per-present-subentry metadata
4. FIMB — file image/data block

The common logical section names are usually written `GARC`, `FATO`, `FATB`, and `FIMB`. On little-endian disk representation, tools/documentation may display the four raw bytes as the reversed ASCII strings `CRAG`, `OTAF`, `BTAF`, and `BMIF`. Code must distinguish a human-readable logical magic from the byte sequence actually read/written.

For Generation VI, pk3DS represents the version field as `0x0400` (`VER_4`) and uses a 0x1C-byte main header. Project Shutan refers to this as "version 4". Until a retail file is available, the repository should preserve both notations and avoid silently treating the raw field as integer `0x0004`.

Both sources describe a four-section archive with a 32-bit bit-vector for each FATB entry. For every set bit, a subentry provides three 32-bit values corresponding to data start, data end, and unpadded length. File data is addressed relative to the archive data region and is commonly padded/aligned.

## Important interpretation difference

Project Shutan describes the FATB bit-vector primarily in terms of language variants for an entry. pk3DS treats it more generally as a **32-slot subentry vector** and extracts entries with multiple populated slots as a directory-like group.

Therefore this project will not encode `bit N == language N` as a universal GARC rule. Language-slot meaning is treated as a higher-level semantic used by some archives, while the container layer exposes up to 32 numbered subentries. Archive-specific semantics must be verified separately.

## Working structural model

### Main header

Research fields currently expected:

- 4-byte magic
- main-header size
- byte-order marker
- version
- section/chunk count
- data offset
- total archive size
- largest-file size information

For Gen VI/version 4, public implementations expect four chunks and a 0x1C-byte main header.

### FATO

Research fields currently expected:

- 4-byte magic
- section size
- 16-bit entry count
- 16-bit padding field
- one 32-bit FATB-relative offset per top-level entry

pk3DS writes the padding field as `0xFFFF`.

### FATB

Research fields currently expected:

- 4-byte magic
- section size
- total contained-file/subfile count
- one record per FATO entry

Each record begins with a 32-bit presence vector. For each set bit, one subentry triple follows:

- start offset
- end offset
- unpadded length

The vector can therefore represent one or multiple payloads under one top-level entry.

### FIMB

Research fields currently expected:

- 4-byte magic
- section/header size (public implementation uses 0x0C)
- data-region size
- packed payload data follows the archive headers

## Padding and compression

pk3DS's version-4 writer aligns payloads to 4 bytes and records unpadded payload length separately. Its unpacker also tests payloads for an LZ-family marker and may decompress them as a second layer. This means **GARC is a container format; compression belongs to individual payloads and should not be conflated with the archive itself**.

## What is not yet project-verified

Without a Pokémon Y source dump, the following remain unverified here:

- exact raw magic bytes in a retail Y archive
- whether all retail Y GARCs use identical padding behavior
- semantics of every FATB bit position in every archive
- ordering rules for payload data
- whether unusual archives deviate from common 4-byte alignment
- exact archive-path-to-purpose mapping under `RomFS/a/...`
- revision/region differences

## Planned independent implementation

The eventual parser/writer should:

1. Parse container structure without assigning archive-specific semantics.
2. Expose FATB subentries as numbered slots 0–31.
3. Preserve unknown/reserved fields and padding.
4. Support deterministic unpack/repack of synthetic fixtures first.
5. Add LZ11 handling as a separate codec layer.
6. Add archive-specific schemas only after source-backed verification.
7. When a lawful Pokémon Y dump becomes available, verify parse → repack behavior and record hashes/revision metadata without committing the ROM itself.

## Verification state

- Container concept: **publicly corroborated**
- Version-4 layout: **publicly corroborated, not yet retail-verified in this repository**
- 32-slot FATB vector: **publicly corroborated**
- universal language-bit interpretation: **not accepted; archive-specific verification required**
- Pokémon Y path inventory: **blocked pending source dump**
