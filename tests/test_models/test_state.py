#!/usr/bin/python3
"""
test module for State class
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    unittest for State model class
    """
    def test_city_id(self):
        """
        test State has id attribute
        """
        a = State()
        self.assertTrue(hasattr(a, 'id'))

    def test_state_created_at(self):
        """
        test State instances have created_at attribute
        """
        a = State()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_state_updated_at(self):
        """
        test State instances have updated_at attribute
        """
        a = State()
        self.assertTrue(hasattr(a, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
