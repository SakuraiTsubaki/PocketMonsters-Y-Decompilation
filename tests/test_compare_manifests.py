import unittest

from tools.compare_manifests import compare


class CompareManifestTests(unittest.TestCase):
    def test_compare_categories(self) -> None:
        left = {"entries": [{"path": "exefs/code.bin", "size": 4, "sha256": "same"}, {"path": "romfs/a.bin", "size": 1, "sha256": "left"}, {"path": "romfs/left.bin", "size": 1, "sha256": "only-left"}]}
        right = {"entries": [{"path": "exefs/code.bin", "size": 4, "sha256": "same"}, {"path": "romfs/a.bin", "size": 2, "sha256": "right"}, {"path": "romfs/right.bin", "size": 1, "sha256": "only-right"}]}
        result = compare(left, right)
        self.assertEqual(result["same"], ["exefs/code.bin"])
        self.assertEqual(result["only_left"], ["romfs/left.bin"])
        self.assertEqual(result["only_right"], ["romfs/right.bin"])
        self.assertEqual(result["changed"][0]["path"], "romfs/a.bin")


if __name__ == "__main__":
    unittest.main()
