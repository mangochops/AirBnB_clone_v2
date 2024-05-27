#!/usr/bin/python3
"""
Unit tests for the Amenity view
"""

import unittest
from api.v1.app import app
from models import storage
from models.amenity import Amenity
import json

class TestAmenityView(unittest.TestCase):
    """Test all API actions for Amenity objects"""

    def setUp(self):
        """Set up the test client"""
        self.client = app.test_client()
        self.client.testing = True

    def test_get_amenities(self):
        """Test retrieving all amenities"""
        response = self.client.get('/api/v1/amenities')
        self.assertEqual(response.status_code, 200)

    def test_get_amenity(self):
        """Test retrieving a single amenity"""
        new_amenity = Amenity(name="Pool")
        new_amenity.save()
        response = self.client.get(f'/api/v1/amenities/{new_amenity.id}')
        self.assertEqual(response.status_code, 200)

    def test_delete_amenity(self):
        """Test deleting an amenity"""
        new_amenity = Amenity(name="Gym")
        new_amenity.save()
        response = self.client.delete(f'/api/v1/amenities/{new_amenity.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(storage.get(Amenity, new_amenity.id))

    def test_create_amenity(self):
        """Test creating a new amenity"""
        response = self.client.post('/api/v1/amenities', json={'name': 'WiFi'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('name', response.get_json())
        self.assertEqual(response.get_json()['name'], 'WiFi')

    def test_update_amenity(self):
        """Test updating an amenity"""
        new_amenity = Amenity(name="Parking")
        new_amenity.save()
        response = self.client.put(f'/api/v1/amenities/{new_amenity.id}', json={'name': 'Free Parking'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['name'], 'Free Parking')

if __name__ == '__main__':
    unittest.main()
