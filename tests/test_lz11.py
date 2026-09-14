import unittest

from tools.lz11 import LZ11Error, decompress_lz11, is_lz11


class LZ11Tests(unittest.TestCase):
    def test_signature(self):
        self.assertTrue(is_lz11(bytes([0x11, 1, 0, 0])))
        self.assertFalse(is_lz11(b""))
        self.assertFalse(is_lz11(bytes([0x10, 1, 0, 0])))

    def test_literal_only(self):
        encoded = bytes([0x11, 3, 0, 0, 0x00]) + b"ABC"
        result = decompress_lz11(encoded)
        self.assertEqual(result.output, b"ABC")
        self.assertEqual(result.trailing, b"")

    def test_short_back_reference(self):
        encoded = bytes([0x11, 6, 0, 0, 0x10]) + b"ABC" + bytes([0x20, 0x02])
        self.assertEqual(decompress_lz11(encoded).output, b"ABCABC")

    def test_medium_length_form(self):
        encoded = bytes([0x11, 18, 0, 0, 0x40, ord("A"), 0x00, 0x00, 0x00])
        self.assertEqual(decompress_lz11(encoded).output, b"A" * 18)

    def test_long_length_form(self):
        size = 1 + 0x111
        encoded = bytes(
            [0x11, size & 0xFF, (size >> 8) & 0xFF, (size >> 16) & 0xFF,
             0x40, ord("A"), 0x10, 0x00, 0x00, 0x00]
        )
        self.assertEqual(decompress_lz11(encoded).output, b"A" * size)

    def test_extended_size_header(self):
        encoded = bytes([0x11, 0, 0, 0, 3, 0, 0, 0, 0x00]) + b"XYZ"
        self.assertEqual(decompress_lz11(encoded).output, b"XYZ")

    def test_trailing_padding_is_reported(self):
        encoded = bytes([0x11, 1, 0, 0, 0x00, ord("Q"), 0xFF, 0xFF])
        result = decompress_lz11(encoded)
        self.assertEqual(result.output, b"Q")
        self.assertEqual(result.trailing, b"\xFF\xFF")
        with self.assertRaises(LZ11Error):
            decompress_lz11(encoded, allow_trailing=False)

    def test_back_reference_before_output_is_rejected(self):
        encoded = bytes([0x11, 3, 0, 0, 0x80, 0x20, 0x00])
        with self.assertRaises(LZ11Error):
            decompress_lz11(encoded)

    def test_truncated_stream_is_rejected(self):
        with self.assertRaises(LZ11Error):
            decompress_lz11(bytes([0x11, 1, 0, 0, 0x00]))


if __name__ == "__main__":
    unittest.main()
