import hashlib
import tempfile
import unittest
from pathlib import Path

from tools.extracted_tree_map import classify, inventory


class ExtractedTreeMapTests(unittest.TestCase):
    def test_classification(self) -> None:
        self.assertEqual(classify(Path("exefs/.code")), ("exefs", "executable-code"))
        self.assertEqual(classify(Path("romfs/a/0/0/0")), ("romfs", "file"))
        self.assertEqual(classify(Path("DecryptedExtHeader.bin")), ("exheader", "system-control"))

    def test_inventory_is_metadata_only_and_skips_keys(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "exefs").mkdir()
            (root / "romfs" / "a").mkdir(parents=True)
            (root / "exefs" / ".code").write_bytes(b"code")
            (root / "romfs" / "a" / "file.bin").write_bytes(b"data")
            (root / "title.keys").write_text("secret", encoding="utf-8")
            result = inventory(root, "synthetic")
            self.assertEqual(result["entry_count"], 2)
            paths = [entry["path"] for entry in result["entries"]]
            self.assertEqual(paths, ["exefs/.code", "romfs/a/file.bin"])
            self.assertEqual(result["entries"][0]["sha256"], hashlib.sha256(b"code").hexdigest())
            self.assertNotIn("secret", str(result))


if __name__ == "__main__":
    unittest.main()
