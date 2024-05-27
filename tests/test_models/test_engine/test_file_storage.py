#!/usr/bin/python3
"""Tests for FileStorage engine"""
import unittest
from models.engine.file_storage import FileStorage
from models.state import State

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.state = State(name="California")
        self.storage.new(self.state)
        self.storage.save()

    def test_get(self):
        """Test get method"""
        self.assertIsNotNone(self.storage.get(State, self.state.id))
        self.assertIsNone(self.storage.get(State, "nonexistent_id"))

    def test_count(self):
        """Test count method"""
        initial_count = self.storage.count()
        self.assertEqual(self.storage.count(State), 1)
        self.assertEqual(initial_count, self.storage.count())

if __name__ == '__main__':
    unittest.main()
