import unittest
from utils import sanitize_query, build_response


class TestUtils(unittest.TestCase):

    def test_sanitize_query_empty(self):
        self.assertEqual(sanitize_query(""), "")

    def test_sanitize_query_strips(self):
        self.assertEqual(sanitize_query("  Hello  "), "hello")

    def test_build_response(self):
        result = build_response("test", ["a", "b"])
        self.assertEqual(result["count"], 2)
        self.assertEqual(result["query"], "test")


if __name__ == "__main__":
    unittest.main()
