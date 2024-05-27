#!/usr/bin/python3
"""Unit tests for the app module"""
import unittest
from api.v1.app import app

class TestApp(unittest.TestCase):
    """Test the app module"""

    def setUp(self):
        """Set up test client"""
        self.client = app.test_client()

    def test_404_error(self):
        """Test the 404 error handler"""
        response = self.client.get('/api/v1/nop')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "Not found"})

if __name__ == "__main__":
    unittest.main()
