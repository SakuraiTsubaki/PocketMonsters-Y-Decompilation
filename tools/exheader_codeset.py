#!/usr/bin/env python3
"""Parse the public, documented CodeSetInfo fields from a 3DS NCCH ExHeader."""

from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path

SCHEMA = "generation6.exheader-codeset.v1"
PAGE_SIZE = 0x1000


def _codeset(blob: bytes, offset: int) -> dict:
    address, pages, size = struct.unpack_from("<III", blob, offset)
    return {
        "address": address,
        "physical_pages": pages,
        "physical_bytes": pages * PAGE_SIZE,
        "size": size,
    }


def parse(blob: bytes) -> dict:
    if len(blob) < 0x40:
        raise ValueError("ExHeader SCI requires at least 0x40 bytes")
    title_raw = blob[0:8].split(b"\0", 1)[0]
    flags = blob[0x0D]
    return {
        "schema": SCHEMA,
        "application_title_ascii": title_raw.decode("ascii", errors="replace"),
        "flags": flags,
        "compress_exefs_code": bool(flags & 0x01),
        "sd_application": bool(flags & 0x02),
        "remaster_version": struct.unpack_from("<H", blob, 0x0E)[0],
        "text": _codeset(blob, 0x10),
        "stack_size": struct.unpack_from("<I", blob, 0x1C)[0],
        "ro": _codeset(blob, 0x20),
        "data": _codeset(blob, 0x30),
        "bss_size": struct.unpack_from("<I", blob, 0x3C)[0],
        "notes": [
            "Fields are parsed from the documented NCCH ExHeader System Control Info layout.",
            "No Pokémon-specific meaning is inferred from these generic CTR fields.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exheader", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    result = parse(args.exheader.read_bytes())
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
