#!/usr/bin/python3
"""
test module for Place class
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    unittest for Place model class
    """
    def test_Place_id(self):
        """
        test Place has id attribute
        """
        a = Place()
        self.assertTrue(hasattr(a, 'id'))

    def test_Place_created_at(self):
        """
        test Place instances have created_at attribute
        """
        a = Place()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_Place_updated_at(self):
        """
        test Place instances have updated_at attribute
        """
        a = Place()
        self.assertTrue(hasattr(a, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
