#!/usr/bin/env python3
"""Validate and summarize the Generation VI decompilation workstream registry."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

REQUIRED_TITLES = {"X", "Y", "OmegaRuby", "AlphaSapphire"}
ALLOWED_STATUS = {"opened", "mapping", "verified", "complete"}


def validate(registry: dict) -> list[str]:
    errors: list[str] = []
    if registry.get("schema") != "generation-vi.workstreams.v1":
        errors.append("unexpected schema")
    titles = set(registry.get("titles", []))
    if titles != REQUIRED_TITLES:
        errors.append("registry titles must be exactly X, Y, OmegaRuby, AlphaSapphire")
    seen: set[str] = set()
    for row in registry.get("workstreams", []):
        ident = row.get("id")
        if not isinstance(ident, str) or not ident:
            errors.append("workstream id missing")
            continue
        if ident in seen:
            errors.append(f"duplicate workstream id: {ident}")
        seen.add(ident)
        row_titles = set(row.get("titles", []))
        if not row_titles or not row_titles <= REQUIRED_TITLES:
            errors.append(f"invalid title scope: {ident}")
        if row.get("status") not in ALLOWED_STATUS:
            errors.append(f"invalid status: {ident}")
        if not row.get("evidence"):
            errors.append(f"missing evidence rule: {ident}")
    if not seen:
        errors.append("no workstreams defined")
    return errors


def summarize(registry: dict) -> dict:
    by_status = Counter(row["status"] for row in registry.get("workstreams", []))
    by_title = {title: 0 for title in sorted(REQUIRED_TITLES)}
    for row in registry.get("workstreams", []):
        for title in row.get("titles", []):
            by_title[title] += 1
    return {"workstream_count": len(registry.get("workstreams", [])), "by_status": dict(sorted(by_status.items())), "by_title": by_title}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("registry", type=Path)
    args = parser.parse_args()
    data = json.loads(args.registry.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(json.dumps(summarize(data), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
