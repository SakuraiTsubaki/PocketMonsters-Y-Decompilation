#!/usr/bin/env python3
"""Build a metadata-only map of an already-extracted Nintendo 3DS title tree."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "generation6.extracted-tree-map.v1"
BLOCKED_NAMES = {"prod.keys", "title.keys"}
BLOCKED_SUFFIXES = {".keys"}
EXEFS_NAMES = {"exefs", "decryptedexefs"}
ROMFS_NAMES = {"romfs", "decryptedromfs"}
EXHEADER_NAMES = {"exheader.bin", "extheader.bin", "decryptedextheader.bin"}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()


def _blocked(path: Path) -> bool:
    return path.name.lower() in BLOCKED_NAMES or path.suffix.lower() in BLOCKED_SUFFIXES


def classify(relative: Path) -> tuple[str, str]:
    parts = [part.lower() for part in relative.parts]
    name = relative.name.lower()
    layer = "container"
    if any(part in EXEFS_NAMES for part in parts):
        layer = "exefs"
    elif any(part in ROMFS_NAMES for part in parts):
        layer = "romfs"

    if name in EXHEADER_NAMES:
        return "exheader", "system-control"
    if layer == "exefs":
        if name in {".code", "code", "code.bin"}:
            return layer, "executable-code"
        if name in {"icon", "icon.bin"}:
            return layer, "icon"
        if name in {"banner", "banner.bin"}:
            return layer, "banner"
        if name in {"logo", "logo.bin"}:
            return layer, "logo"
    return layer, "file"


def inventory(root: Path, title: str | None = None) -> dict:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError("target must be an extracted directory")

    entries = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink() or _blocked(path):
            continue
        relative = path.relative_to(root)
        layer, role = classify(relative)
        entries.append({
            "path": relative.as_posix(),
            "size": path.stat().st_size,
            "sha256": sha256_file(path),
            "layer": layer,
            "role": role,
        })

    layer_counts = Counter(entry["layer"] for entry in entries)
    layer_bytes = Counter()
    for entry in entries:
        layer_bytes[entry["layer"]] += entry["size"]

    return {
        "schema": SCHEMA,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "title": title,
        "entry_count": len(entries),
        "total_bytes": sum(entry["size"] for entry in entries),
        "layers": {
            layer: {"files": layer_counts[layer], "bytes": layer_bytes[layer]}
            for layer in sorted(layer_counts)
        },
        "entries": entries,
        "notes": [
            "This manifest contains hashes, sizes, roles, and relative paths only.",
            "Layer/role labels are structural hints and do not prove game-specific semantics.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--title")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    result = inventory(args.root, args.title)
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
