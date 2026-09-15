import struct
import unittest

from tools.exheader_codeset import PAGE_SIZE, parse


class ExHeaderCodeSetTests(unittest.TestCase):
    def test_parse_documented_sci_fields(self) -> None:
        blob = bytearray(0x40)
        blob[0:8] = b"TESTAPP\0"
        blob[0x0D] = 0x03
        struct.pack_into("<H", blob, 0x0E, 7)
        struct.pack_into("<III", blob, 0x10, 0x00100000, 2, 0x1800)
        struct.pack_into("<I", blob, 0x1C, 0x4000)
        struct.pack_into("<III", blob, 0x20, 0x00102000, 1, 0x800)
        struct.pack_into("<III", blob, 0x30, 0x00103000, 3, 0x2200)
        struct.pack_into("<I", blob, 0x3C, 0x600)
        result = parse(bytes(blob))
        self.assertEqual(result["application_title_ascii"], "TESTAPP")
        self.assertTrue(result["compress_exefs_code"])
        self.assertTrue(result["sd_application"])
        self.assertEqual(result["text"]["physical_bytes"], 2 * PAGE_SIZE)
        self.assertEqual(result["ro"]["address"], 0x00102000)
        self.assertEqual(result["data"]["size"], 0x2200)
        self.assertEqual(result["bss_size"], 0x600)

    def test_rejects_short_input(self) -> None:
        with self.assertRaises(ValueError):
            parse(b"\0" * 0x3F)


if __name__ == "__main__":
    unittest.main()
