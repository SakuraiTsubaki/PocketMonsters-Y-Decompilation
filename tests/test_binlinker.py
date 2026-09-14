import unittest

from tools.binlinker import BinLinkerError, candidate_byteorders, parse_binlinker_header


class BinLinkerTests(unittest.TestCase):
    def test_little_endian_header(self):
        data = (
            b"AD"
            + (2).to_bytes(2, "little")
            + (12).to_bytes(4, "little")
            + (20).to_bytes(4, "little")
            + b"\x00" * 20
        )
        header = parse_binlinker_header(data, byteorder="little")
        self.assertEqual(header.magic, "AD")
        self.assertEqual(header.file_count, 2)
        self.assertEqual(header.offsets, (12, 20))
        self.assertEqual(header.table_end, 12)

    def test_big_endian_header_is_supported_explicitly(self):
        data = (
            b"ZZ"
            + (2).to_bytes(2, "big")
            + (12).to_bytes(4, "big")
            + (20).to_bytes(4, "big")
            + b"\x00" * 20
        )
        header = parse_binlinker_header(data, byteorder="big")
        self.assertEqual(header.offsets, (12, 20))

    def test_candidate_byteorder_is_only_structural(self):
        data = (
            b"AD"
            + (2).to_bytes(2, "little")
            + (12).to_bytes(4, "little")
            + (20).to_bytes(4, "little")
            + b"\x00" * 20
        )
        self.assertEqual(candidate_byteorders(data), ("little",))

    def test_truncated_offset_table_is_rejected(self):
        data = b"AD" + (3).to_bytes(2, "little") + (8).to_bytes(4, "little")
        with self.assertRaises(BinLinkerError):
            parse_binlinker_header(data, byteorder="little")

    def test_offset_semantics_are_not_invented(self):
        data = (
            b"XY"
            + (2).to_bytes(2, "little")
            + (100).to_bytes(4, "little")
            + (4).to_bytes(4, "little")
        )
        header = parse_binlinker_header(data, byteorder="little")
        self.assertEqual(header.offsets, (100, 4))


if __name__ == "__main__":
    unittest.main()
