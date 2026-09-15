import unittest

from tools.workstream_registry import summarize, validate


class WorkstreamRegistryTests(unittest.TestCase):
    def test_valid_registry(self) -> None:
        registry = {"schema":"generation-vi.workstreams.v1","titles":["X","Y","OmegaRuby","AlphaSapphire"],"workstreams":[{"id":"common","titles":["X","Y","OmegaRuby","AlphaSapphire"],"status":"opened","evidence":"direct evidence"},{"id":"xy","titles":["X","Y"],"status":"mapping","evidence":"paired evidence"}]}
        self.assertEqual(validate(registry), [])
        summary = summarize(registry)
        self.assertEqual(summary["workstream_count"], 2)
        self.assertEqual(summary["by_title"]["X"], 2)
        self.assertEqual(summary["by_title"]["AlphaSapphire"], 1)

    def test_duplicate_and_bad_scope_are_rejected(self) -> None:
        registry = {"schema":"generation-vi.workstreams.v1","titles":["X","Y","OmegaRuby","AlphaSapphire"],"workstreams":[{"id":"dup","titles":["X"],"status":"opened","evidence":"a"},{"id":"dup","titles":["Invalid"],"status":"unknown","evidence":""}]}
        errors = validate(registry)
        self.assertTrue(any("duplicate" in error for error in errors))
        self.assertTrue(any("invalid title scope" in error for error in errors))
        self.assertTrue(any("invalid status" in error for error in errors))
        self.assertTrue(any("missing evidence" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
