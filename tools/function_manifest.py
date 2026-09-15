#!/usr/bin/env python3
"""Normalize and validate evidence-based function records for Gen VI decompilation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SCHEMA = "generation6.function-manifest.v1"
VALID_STATUSES = {"provisional", "observed", "reproduced", "matched"}


def provisional_name(address: int) -> str:
    return f"sub_{address:08X}"


def normalize(records: list[dict], *, text_start: int | None = None, text_size: int | None = None) -> dict:
    normalized = []
    for raw in records:
        address = int(raw["address"], 0) if isinstance(raw["address"], str) else int(raw["address"])
        size = int(raw["size"], 0) if isinstance(raw["size"], str) else int(raw["size"])
        if address < 0 or size <= 0:
            raise ValueError("function address must be non-negative and size must be positive")
        status = raw.get("status", "provisional")
        if status not in VALID_STATUSES:
            raise ValueError(f"invalid function status: {status}")
        symbol = raw.get("symbol") or provisional_name(address)
        evidence = raw.get("evidence", [])
        if not isinstance(evidence, list):
            raise ValueError("evidence must be a list")
        normalized.append({"address": address, "end_address": address + size, "size": size, "symbol": symbol, "status": status, "evidence": evidence, "notes": raw.get("notes")})
    normalized.sort(key=lambda item: (item["address"], item["size"], item["symbol"]))
    overlaps = []
    for left, right in zip(normalized, normalized[1:]):
        if right["address"] < left["end_address"]:
            overlaps.append({"left": left["symbol"], "right": right["symbol"], "range": [right["address"], min(left["end_address"], right["end_address"])]})
    result = {"schema": SCHEMA, "function_count": len(normalized), "functions": normalized, "overlaps": overlaps, "notes": ["Default sub_XXXXXXXX names are neutral provisional identifiers, not semantic claims.", "Semantic renames require evidence and should retain provenance in the evidence field."]}
    if text_start is not None or text_size is not None:
        if text_start is None or text_size is None or text_size <= 0:
            raise ValueError("text_start and positive text_size must be supplied together")
        text_end = text_start + text_size
        outside = [item["symbol"] for item in normalized if item["address"] < text_start or item["end_address"] > text_end]
        unique_covered = 0
        cursor = text_start
        for item in normalized:
            start = max(text_start, item["address"])
            end = min(text_end, item["end_address"])
            if end <= start:
                continue
            if start < cursor:
                start = cursor
            if end > start:
                unique_covered += end - start
                cursor = end
        result["text_range"] = {"start": text_start, "end": text_end, "size": text_size}
        result["outside_text_range"] = outside
        result["unique_covered_bytes"] = unique_covered
        result["coverage_ratio"] = unique_covered / text_size
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON list of function records or object containing a functions list")
    parser.add_argument("--text-start", type=lambda value: int(value, 0))
    parser.add_argument("--text-size", type=lambda value: int(value, 0))
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    records = payload["functions"] if isinstance(payload, dict) else payload
    if not isinstance(records, list):
        raise ValueError("input must contain a function list")
    result = normalize(records, text_start=args.text_start, text_size=args.text_size)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
