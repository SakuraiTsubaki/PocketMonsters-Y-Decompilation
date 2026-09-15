import unittest
from tools.function_manifest import normalize, provisional_name

class FunctionManifestTests(unittest.TestCase):
    def test_provisional_names_and_sorting(self) -> None:
        result = normalize([{"address": "0x1010", "size": 4}, {"address": 0x1000, "size": 8, "symbol": "KnownByEvidence", "status": "observed", "evidence": ["xref:test"]}])
        self.assertEqual(result["functions"][0]["symbol"], "KnownByEvidence")
        self.assertEqual(result["functions"][1]["symbol"], provisional_name(0x1010))
        self.assertEqual(result["overlaps"], [])
    def test_overlap_and_coverage(self) -> None:
        result = normalize([{"address": 0x1000, "size": 0x10}, {"address": 0x1008, "size": 0x10}, {"address": 0x1020, "size": 0x10}], text_start=0x1000, text_size=0x40)
        self.assertEqual(len(result["overlaps"]), 1)
        self.assertEqual(result["unique_covered_bytes"], 0x28)
        self.assertEqual(result["coverage_ratio"], 0x28 / 0x40)
    def test_rejects_invalid_status(self) -> None:
        with self.assertRaises(ValueError):
            normalize([{"address": 0x1000, "size": 4, "status": "guessed"}])
    def test_reports_outside_text_range(self) -> None:
        result = normalize([{"address": 0x0FF0, "size": 0x20}], text_start=0x1000, text_size=0x100)
        self.assertEqual(result["outside_text_range"], ["sub_00000FF0"])

if __name__ == "__main__":
    unittest.main()
