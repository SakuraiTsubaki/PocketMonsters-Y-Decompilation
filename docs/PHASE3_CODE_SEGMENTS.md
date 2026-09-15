# Phase 3 — Executable Code Segment Map

Phase 3 turns a verified, decompressed ExeFS code image into a reproducible metadata map suitable for later disassembly/decompilation work.

## Tool

`tools/code_segment_map.py` combines a locally supplied ExHeader with a locally supplied decompressed ExeFS code image. It does not commit or redistribute code bytes.

The output records, for each documented CodeSetInfo region:

- file offset inside the decompressed code image
- virtual address
- physical page count and physical byte span
- logical size
- SHA-256 of the physical span
- SHA-256 of the logical bytes

The three mapped regions are kept under neutral platform names: `text`, `ro`, and `data`. BSS size is recorded separately because it is not initialized from code-image bytes.

## Compression rule

If the ExHeader marks ExeFS code as compressed, the mapper refuses to continue unless the caller explicitly confirms that the input has already been decompressed with `--decompressed`. This prevents compressed bytes from being mistaken for executable segment layout.

## Parallel Generation VI workflow

Run the same process independently for X, Y, Omega Ruby, and Alpha Sapphire. Compare resulting segment addresses, sizes, and hashes in this order:

1. X ↔ Y
2. Omega Ruby ↔ Alpha Sapphire
3. verified XY-common ↔ verified ORAS-common

Only then promote findings to XY common, ORAS common, or Generation VI common.

## Next executable step

Once a real target supplies verified segment maps, begin ARM11 function-boundary and cross-reference work with provisional evidence-based symbols. Function names must not be invented from community guesses alone; every rename should retain provenance to an observed code range and supporting evidence.
