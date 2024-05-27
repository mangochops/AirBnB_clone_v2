#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_city_instantiation(self):
        """Test that City instances are correctly instantiated"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_city_attributes(self):
        """Test City attributes"""
        city = City()
        city.name = "San Francisco"
        city.state_id = "123"
        self.assertEqual(city.name, "San Francisco")
        self.assertEqual(city.state_id, "123")

if __name__ == "__main__":
    unittest.main()
