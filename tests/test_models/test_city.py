#!/usr/bin/python3
"""
test module for City class
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    unittest for City model class
    """
    def test_city_id(self):
        """
        test City has id attribute
        """
        a = City()
        self.assertTrue(hasattr(a, 'id'))

    def test_city_created_at(self):
        """
        test City instances have created_at attribute
        """
        a = City()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_city_updated_at(self):
        """
        test City instances have updated_at attribute
        """
        a = City()
        self.assertTrue(hasattr(a, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
