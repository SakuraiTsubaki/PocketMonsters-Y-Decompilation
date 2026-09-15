# Binary Linked archives (BinLinker / BL)

## Status

**Public-research baseline; not yet verified against a local Pokémon Y dump.**

This document records only format details supported by public reverse-engineering material. Any game-specific magic values, archive inventories, offsets, or file-role assignments remain provisional until they can be checked against an owned dump.

## Purpose

A BinLinker is a lightweight binary container used to place several related binary payloads into one blob and reach them through an offset table rather than filenames.

Public Gen VI research describes this family as inherited from earlier Game Freak titles and still used in Pokémon X/Y and later games.

## Publicly documented header

| Offset | Type | Meaning | Confidence |
|---:|---|---|---|
| `0x00` | `char[2]` | variable two-byte magic identifying a content family | documented |
| `0x02` | `uint16` | number of stored payloads | documented |
| `0x04` | `uint32[fileCount]` | starting offsets for payloads | documented |

Conceptual representation:

```text
+0x00  magic[2]
+0x02  fileCount
+0x04  fileOffsets[fileCount]
...    payload data
```

## Important limitations

- The two-byte magic is not a universal constant; it varies with the content family.
- Public documentation states that BinLinker containers do not carry ordinary filenames.
- Public documentation commonly associates these containers with `.pack` files, but this repository will not assume every `.pack` is a BinLinker until verified.
- The public description does not fully settle offset base semantics, alignment rules, padding, duplicate offsets, empty entries, or how the final payload length is encoded/inferred.
- Endianness will be recorded only after independent implementation/sample verification rather than assumed from platform convention.

## Parser design requirements

A future parser should:

1. read the two-byte magic without restricting it to a hard-coded list;
2. read `fileCount` with an explicitly selected byte order;
3. reject an offset table that exceeds the input length;
4. preserve the original offset table exactly;
5. expose payload boundaries without inventing filenames;
6. preserve unknown padding and trailing data;
7. distinguish observed facts from inferred boundaries.

Until a real sample is available, the parser must support synthetic test fixtures and must not claim byte-perfect Pokémon Y compatibility.

## Verification plan

When a lawful local dump is available:

1. inventory candidate `.pack` files;
2. identify recurring two-byte magics;
3. test byte order and offset base;
4. compare consecutive offsets with real payload boundaries;
5. check alignment/padding behavior;
6. map magic values to content families only after repeated evidence;
7. compare X/Y and ORAS behavior separately.

## Sources

- TeamEXR, Project Shutan development wiki: `How Pokemon XY works/Archive formats/Binary Linked archives (BLs).md`
- Cross-check future implementations against independent parsers when located; do not treat a single wiki page as final specification.
