"""Unit tests for "search_lines" generator."""
import unittest
import io
from src.explorer import search_lines


class TestExplorer(unittest.TestCase):
    """Test case to check "search_lines" generator."""

    def setUp(self):
        """Creates "file" for tests from string"""
        self.source = io.StringIO("Присоединяйтесь к проекту VK\n"
                                  "VK - это более 200 проектов и продуктов\n"
                                  "Приглашаем создавать прорывные ПРОекты\n")

    def test_generativity(self):
        """Tests that function is generator and it finds correct strings"""
        iterator = search_lines(["VK"], file=self.source)
        self.assertEqual(next(iterator), "Присоединяйтесь к проекту VK")
        self.assertEqual(
            next(iterator), "VK - это более 200 проектов и продуктов")
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_lower_case_search(self):
        """Tests case-independency of search."""
        self.assertEqual(list(search_lines(["ПроектЫ"], file=self.source)),
                         ["Приглашаем создавать прорывные ПРОекты"])

    def test_particular_words(self):
        """Tests that function doesn't find subwords."""
        self.assertEqual(list(search_lines(["проект"], file=self.source)), [])

    def test_over_part_words(self):
        """Tests that function doesn't find words with additional letters."""
        self.assertEqual(list(search_lines(["проектымана"],
                                           file=self.source)), [])
