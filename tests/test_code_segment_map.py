import hashlib
import struct
import unittest

from tools.code_segment_map import map_code


def make_exheader(compressed: bool = False) -> bytes:
    blob = bytearray(0x40)
    blob[0:8] = b"TESTAPP\0"
    blob[0x0D] = 0x01 if compressed else 0x00
    struct.pack_into("<III", blob, 0x10, 0x00100000, 1, 3)
    struct.pack_into("<III", blob, 0x20, 0x00101000, 1, 2)
    struct.pack_into("<III", blob, 0x30, 0x00102000, 1, 4)
    struct.pack_into("<I", blob, 0x3C, 0x500)
    return bytes(blob)


class CodeSegmentMapTests(unittest.TestCase):
    def test_maps_three_physical_pages(self) -> None:
        code = b"A" * 0x1000 + b"B" * 0x1000 + b"C" * 0x1000
        result = map_code(make_exheader(), code)
        self.assertEqual(result["mapped_physical_bytes"], 0x3000)
        self.assertEqual(result["trailing_bytes"], 0)
        self.assertEqual([s["file_offset"] for s in result["segments"]], [0, 0x1000, 0x2000])
        self.assertEqual(result["segments"][0]["sha256_logical"], hashlib.sha256(b"AAA").hexdigest())
        self.assertEqual(result["segments"][2]["virtual_address"], 0x00102000)
        self.assertEqual(result["bss_size"], 0x500)

    def test_requires_decompressed_confirmation(self) -> None:
        code = b"X" * 0x3000
        with self.assertRaises(ValueError):
            map_code(make_exheader(compressed=True), code)
        result = map_code(make_exheader(compressed=True), code, decompressed=True)
        self.assertTrue(result["compress_exefs_code"])

    def test_rejects_short_code(self) -> None:
        with self.assertRaises(ValueError):
            map_code(make_exheader(), b"X" * 0x2000)


if __name__ == "__main__":
    unittest.main()
