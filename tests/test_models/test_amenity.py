#!/usr/bin/python3
"""
test module for Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    unittest for Amenity model class
    """
    def test_amenity_id(self):
        """
        test Amenity has id attribute
        """
        a = Amenity()
        self.assertTrue(hasattr(a, 'id'))

    def test_amenity_created_at(self):
        """
        test Amenity instances have created_at attribute
        """
        a = Amenity()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_amenity_updated_at(self):
        """
        test Amenity instances have updated_at attribute
        """
        a = Amenity()
        self.assertTrue(hasattr(a, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
