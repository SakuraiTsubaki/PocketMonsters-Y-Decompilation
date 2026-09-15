#!/usr/bin/env python3
"""Map a decompressed 3DS ExeFS code image into text/ro/data segments using ExHeader CodeSetInfo."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from tools.exheader_codeset import parse as parse_exheader

SCHEMA = "generation6.code-segment-map.v1"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def map_code(exheader: bytes, code: bytes, *, decompressed: bool = False) -> dict:
    info = parse_exheader(exheader)
    if info["compress_exefs_code"] and not decompressed:
        raise ValueError("ExHeader marks ExeFS code as compressed; provide a decompressed code image and set decompressed=True")

    segments = []
    file_offset = 0
    for name in ("text", "ro", "data"):
        spec = info[name]
        physical = spec["physical_bytes"]
        logical = spec["size"]
        if logical > physical:
            raise ValueError(f"{name} logical size exceeds physical region size")
        end = file_offset + physical
        if end > len(code):
            raise ValueError(f"code image is too short for {name} segment")
        physical_blob = code[file_offset:end]
        logical_blob = physical_blob[:logical]
        segments.append({
            "name": name,
            "file_offset": file_offset,
            "virtual_address": spec["address"],
            "physical_pages": spec["physical_pages"],
            "physical_bytes": physical,
            "logical_size": logical,
            "sha256_physical": _sha256(physical_blob),
            "sha256_logical": _sha256(logical_blob),
        })
        file_offset = end

    return {
        "schema": SCHEMA,
        "application_title_ascii": info["application_title_ascii"],
        "remaster_version": info["remaster_version"],
        "compress_exefs_code": info["compress_exefs_code"],
        "input_code_bytes": len(code),
        "mapped_physical_bytes": file_offset,
        "trailing_bytes": len(code) - file_offset,
        "bss_size": info["bss_size"],
        "segments": segments,
        "notes": [
            "Input must be the decompressed ExeFS code image when the ExHeader compression flag is set.",
            "Segment boundaries come only from documented ExHeader CodeSetInfo physical page counts.",
            "No function or Pokémon-specific symbol names are inferred here.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exheader", type=Path)
    parser.add_argument("code", type=Path)
    parser.add_argument("--decompressed", action="store_true", help="confirm that compressed ExeFS code has already been decompressed")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    result = map_code(args.exheader.read_bytes(), args.code.read_bytes(), decompressed=args.decompressed)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
