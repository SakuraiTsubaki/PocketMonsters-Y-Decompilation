#!/usr/bin/env python3
"""Create a reproducible identity manifest for a local Pokémon Y target.

This tool deliberately does not extract, decrypt, repack, or redistribute game
content. It records sizes and SHA-256 digests for a user-supplied local file or
an already-extracted directory so later decompilation work can be tied to an
exact target revision.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

SCHEMA = "pocketmonsters-y.target-inventory.v1"
BLOCKED_NAMES = {"prod.keys", "title.keys"}
BLOCKED_SUFFIXES = {".keys"}


def _is_blocked(path: Path) -> bool:
    name = path.name.lower()
    return name in BLOCKED_NAMES or path.suffix.lower() in BLOCKED_SUFFIXES


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def _iter_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if path.is_file():
            yield path


def inventory(target: Path, label: str | None = None) -> dict:
    target = target.resolve()
    if not target.exists():
        raise FileNotFoundError(target)

    if target.is_file():
        if _is_blocked(target):
            raise ValueError(f"refusing to inventory key material: {target.name}")
        entries = [{"path": target.name, "size": target.stat().st_size, "sha256": sha256_file(target)}]
        kind = "file"
    elif target.is_dir():
        entries = []
        for path in _iter_files(target):
            if _is_blocked(path):
                continue
            entries.append({"path": path.relative_to(target).as_posix(), "size": path.stat().st_size, "sha256": sha256_file(path)})
        kind = "directory"
    else:
        raise ValueError(f"unsupported target type: {target}")

    return {
        "schema": SCHEMA,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target_label": label,
        "target_kind": kind,
        "entry_count": len(entries),
        "total_bytes": sum(entry["size"] for entry in entries),
        "entries": entries,
        "notes": [
            "No game content is embedded in this manifest.",
            "Hashes identify the local source used for reverse engineering.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="local game image or extracted directory")
    parser.add_argument("--label", help="human-readable target/revision label")
    parser.add_argument("-o", "--output", type=Path, help="write JSON manifest here")
    args = parser.parse_args()

    manifest = inventory(args.target, args.label)
    text = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
