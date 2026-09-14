#!/usr/bin/env python3
"""Conservative BinLinker header inspector for Generation VI research.

This tool intentionally parses only the publicly documented header fields.
It does not assume offset base, payload alignment, or file boundary semantics
that have not yet been verified against a lawful local dump.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


class BinLinkerError(ValueError):
    """Raised when a candidate BinLinker header is structurally impossible."""


@dataclass(frozen=True)
class BinLinkerHeader:
    magic: str
    file_count: int
    offsets: tuple[int, ...]
    byteorder: str
    table_end: int


def parse_binlinker_header(data: bytes, *, byteorder: str) -> BinLinkerHeader:
    if byteorder not in {"little", "big"}:
        raise ValueError("byteorder must be 'little' or 'big'")
    if len(data) < 4:
        raise BinLinkerError("truncated BinLinker header")

    file_count = int.from_bytes(data[2:4], byteorder)
    table_end = 4 + (file_count * 4)
    if table_end > len(data):
        raise BinLinkerError(
            f"offset table needs {table_end} bytes but input has {len(data)}"
        )

    offsets = tuple(
        int.from_bytes(data[pos : pos + 4], byteorder)
        for pos in range(4, table_end, 4)
    )
    magic = data[:2].decode("latin-1")
    return BinLinkerHeader(magic, file_count, offsets, byteorder, table_end)


def candidate_byteorders(data: bytes) -> tuple[str, ...]:
    candidates: list[str] = []
    for order in ("little", "big"):
        try:
            parse_binlinker_header(data, byteorder=order)
        except BinLinkerError:
            continue
        candidates.append(order)
    return tuple(candidates)


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect a BinLinker header")
    parser.add_argument("input", type=Path)
    parser.add_argument("--byteorder", choices=("little", "big"))
    args = parser.parse_args()

    data = args.input.read_bytes()
    if args.byteorder is None:
        print(json.dumps({"candidate_byteorders": candidate_byteorders(data)}, indent=2))
        return 0

    header = parse_binlinker_header(data, byteorder=args.byteorder)
    payload = asdict(header)
    payload["offsets"] = list(header.offsets)
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
