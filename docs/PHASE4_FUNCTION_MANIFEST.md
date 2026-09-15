# Phase 4 — Function Boundary and Symbol Manifest

Phase 4 provides the normalized record format used when real ARM11 executable analysis begins for Pokémon X, Y, Omega Ruby, and Alpha Sapphire.

## Principle

Function boundaries and semantic names are separate claims. A function may be recorded as soon as an address and size are observed, while its neutral identifier remains `sub_XXXXXXXX`. A semantic rename is allowed only when evidence supports it.

## Tool

`tools/function_manifest.py` accepts a JSON function list and produces a deterministic manifest containing start/end address, size, symbol, validation status (`provisional`, `observed`, `reproduced`, `matched`), evidence records, overlap diagnostics, and optional text-segment coverage/out-of-range diagnostics.

## Promotion rule

1. Record independently observed function boundaries per exact title/revision.
2. Keep neutral provisional names until evidence supports a semantic rename.
3. Compare X↔Y and OR↔AS only after each side has its own manifest.
4. Promote corresponding behavior to XY common, ORAS common, or Generation VI common only with direct cross-title evidence.

## Next step with real binaries

Once the verified local `.code` text segment is available, function-boundary discovery, call/xref extraction, strings/data references, and reconstructed source files can begin. Every reconstructed function should retain a link back to its exact observed address range and target identity.
