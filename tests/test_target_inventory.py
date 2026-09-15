import hashlib
import tempfile
import unittest
from pathlib import Path

from tools.target_inventory import SCHEMA, inventory, sha256_file


class TargetInventoryTests(unittest.TestCase):
    def test_sha256_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample.bin"
            target.write_bytes(b"abc")
            self.assertEqual(sha256_file(target), hashlib.sha256(b"abc").hexdigest())

    def test_inventory_single_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "pokemon-y.3ds"
            target.write_bytes(b"test-data")
            result = inventory(target, "local-test")
            self.assertEqual(result["schema"], SCHEMA)
            self.assertEqual(result["target_label"], "local-test")
            self.assertEqual(result["target_kind"], "file")
            self.assertEqual(result["entry_count"], 1)
            self.assertEqual(result["total_bytes"], len(b"test-data"))
            self.assertEqual(result["entries"][0]["path"], "pokemon-y.3ds")
            self.assertEqual(result["entries"][0]["sha256"], hashlib.sha256(b"test-data").hexdigest())

    def test_inventory_directory_is_sorted_and_skips_key_material(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "extract"
            (root / "romfs").mkdir(parents=True)
            (root / "exefs").mkdir(parents=True)
            (root / "romfs" / "b.bin").write_bytes(b"b")
            (root / "exefs" / "a.bin").write_bytes(b"a")
            (root / "prod.keys").write_text("do-not-record", encoding="utf-8")
            result = inventory(root)
            self.assertEqual([entry["path"] for entry in result["entries"]], ["exefs/a.bin", "romfs/b.bin"])
            self.assertEqual(result["entry_count"], 2)

    def test_inventory_rejects_key_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "title.keys"
            target.write_text("secret", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "key material"):
                inventory(target)


if __name__ == "__main__":
    unittest.main()
