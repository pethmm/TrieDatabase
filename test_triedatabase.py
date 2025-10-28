# test_triedatabase.py
"""
Tests for TrieDatabase module.
"""

import unittest
from triedatabase import TrieDatabase

class TestTrieDatabase(unittest.TestCase):
    """Test cases for TrieDatabase class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TrieDatabase()
        self.assertIsInstance(instance, TrieDatabase)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TrieDatabase()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
