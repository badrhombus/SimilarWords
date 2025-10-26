"""
Tests for the SimilarWords library.
"""

import unittest
from similar_words import SimilarWords


class TestSimilarWords(unittest.TestCase):
    """Test cases for the SimilarWords class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.sw = SimilarWords()
    
    def test_get_synonyms_basic(self):
        """Test basic synonym retrieval."""
        synonyms = self.sw.get_synonyms("happy")
        self.assertIsInstance(synonyms, list)
        self.assertTrue(len(synonyms) > 0)
        # Check that common synonyms are present
        self.assertTrue(any(word in ["glad", "pleased", "felicitous"] for word in synonyms))
    
    def test_get_synonyms_with_limit(self):
        """Test synonym retrieval with limit."""
        synonyms = self.sw.get_synonyms("good", limit=5)
        self.assertIsInstance(synonyms, list)
        self.assertLessEqual(len(synonyms), 5)
    
    def test_get_synonyms_nonexistent_word(self):
        """Test synonym retrieval for nonexistent word."""
        synonyms = self.sw.get_synonyms("xyzabc123")
        self.assertIsInstance(synonyms, list)
        self.assertEqual(len(synonyms), 0)
    
    def test_get_definitions(self):
        """Test definition retrieval."""
        definitions = self.sw.get_definitions("computer")
        self.assertIsInstance(definitions, list)
        self.assertTrue(len(definitions) > 0)
        # Definitions should be strings
        self.assertTrue(all(isinstance(d, str) for d in definitions))
    
    def test_get_definitions_nonexistent_word(self):
        """Test definition retrieval for nonexistent word."""
        definitions = self.sw.get_definitions("xyzabc123")
        self.assertIsInstance(definitions, list)
        self.assertEqual(len(definitions), 0)
    
    def test_get_related_words(self):
        """Test related words retrieval."""
        related = self.sw.get_related_words("dog")
        self.assertIsInstance(related, list)
        self.assertTrue(len(related) > 0)
    
    def test_get_related_words_with_limit(self):
        """Test related words retrieval with limit."""
        related = self.sw.get_related_words("car", limit=10)
        self.assertIsInstance(related, list)
        self.assertLessEqual(len(related), 10)
    
    def test_get_related_words_nonexistent_word(self):
        """Test related words retrieval for nonexistent word."""
        related = self.sw.get_related_words("xyzabc123")
        self.assertIsInstance(related, list)
        self.assertEqual(len(related), 0)
    
    def test_synonyms_dont_include_original(self):
        """Test that synonyms don't include the original word."""
        word = "happy"
        synonyms = self.sw.get_synonyms(word)
        # Check case-insensitive
        self.assertNotIn(word.lower(), [s.lower() for s in synonyms])
    
    def test_related_words_dont_include_original(self):
        """Test that related words don't include the original word."""
        word = "dog"
        related = self.sw.get_related_words(word)
        # Check case-insensitive
        self.assertNotIn(word.lower(), [r.lower() for r in related])


if __name__ == "__main__":
    unittest.main()
