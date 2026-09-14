#!/usr/bin/env python3
"""Clean-room Nintendo LZ11 (0x11) decoder for project research.

The implementation is based on publicly documented format behavior and is
intentionally independent from retail ROM data. It is suitable for synthetic
fixtures now and for later validation against lawfully obtained local dumps.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


class LZ11Error(ValueError):
    """Raised when an LZ11 stream is malformed or inconsistent."""


@dataclass(frozen=True)
class LZ11Result:
    output: bytes
    consumed: int
    trailing: bytes


def is_lz11(data: bytes) -> bool:
    """Return True when *data* has a minimally valid LZ11 signature/header."""
    return len(data) >= 4 and data[0] == 0x11


def _read_declared_size(data: bytes) -> tuple[int, int]:
    if len(data) < 4:
        raise LZ11Error("truncated LZ11 header")
    if data[0] != 0x11:
        raise LZ11Error(f"invalid LZ11 type byte: 0x{data[0]:02X}")

    size = data[1] | (data[2] << 8) | (data[3] << 16)
    pos = 4
    if size == 0:
        if len(data) < 8:
            raise LZ11Error("truncated extended LZ11 size")
        size = int.from_bytes(data[4:8], "little")
        pos = 8
    return size, pos


def decompress_lz11(data: bytes, *, allow_trailing: bool = True) -> LZ11Result:
    """Decompress an LZ11 stream and report consumed/trailing bytes.

    Flag bits are consumed MSB-first. Literal blocks copy one byte. Compressed
    blocks use a 12-bit backwards distance plus one and one of the three LZ11
    length encodings selected by the first nibble.
    """
    target_size, pos = _read_declared_size(data)
    out = bytearray()

    while len(out) < target_size:
        if pos >= len(data):
            raise LZ11Error("missing flag byte")
        flags = data[pos]
        pos += 1

        for bit in range(7, -1, -1):
            if len(out) == target_size:
                break

            if not (flags & (1 << bit)):
                if pos >= len(data):
                    raise LZ11Error("truncated literal block")
                out.append(data[pos])
                pos += 1
                continue

            if pos >= len(data):
                raise LZ11Error("truncated back-reference")

            b1 = data[pos]
            pos += 1
            indicator = b1 >> 4

            if indicator == 0:
                if pos + 2 > len(data):
                    raise LZ11Error("truncated medium back-reference")
                b2, b3 = data[pos], data[pos + 1]
                pos += 2
                length = (((b1 & 0x0F) << 4) | (b2 >> 4)) + 0x11
                distance = (((b2 & 0x0F) << 8) | b3) + 1
            elif indicator == 1:
                if pos + 3 > len(data):
                    raise LZ11Error("truncated long back-reference")
                b2, b3, b4 = data[pos], data[pos + 1], data[pos + 2]
                pos += 3
                length = (
                    ((b1 & 0x0F) << 12) | (b2 << 4) | (b3 >> 4)
                ) + 0x111
                distance = (((b3 & 0x0F) << 8) | b4) + 1
            else:
                if pos >= len(data):
                    raise LZ11Error("truncated short back-reference")
                b2 = data[pos]
                pos += 1
                length = indicator + 1
                distance = (((b1 & 0x0F) << 8) | b2) + 1

            if distance > 0x1000:
                raise LZ11Error("back-reference distance exceeds 0x1000")
            if distance > len(out):
                raise LZ11Error("back-reference points before output start")
            if len(out) + length > target_size:
                raise LZ11Error("back-reference exceeds declared output size")

            for _ in range(length):
                out.append(out[-distance])

    trailing = data[pos:]
    if trailing and not allow_trailing:
        raise LZ11Error("trailing bytes after compressed stream")

    return LZ11Result(bytes(out), pos, trailing)


def main() -> int:
    parser = argparse.ArgumentParser(description="Decompress Nintendo LZ11 data")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--reject-trailing",
        action="store_true",
        help="fail if bytes remain after the compressed stream",
    )
    args = parser.parse_args()

    result = decompress_lz11(
        args.input.read_bytes(), allow_trailing=not args.reject_trailing
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(result.output)
    print(
        f"decoded={len(result.output)} consumed={result.consumed} "
        f"trailing={len(result.trailing)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
