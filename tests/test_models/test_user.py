#!/usr/bin/python3
"""
test module for user class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    unittest for User model class
    """
    def test_user_id(self):
        """
        test User has id attribute
        """
        a = User()
        self.assertTrue(hasattr(a, 'id'))

    def test_user_created_at(self):
        """
        test User instances have created_at attribute
        """
        a = User()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_User_updated_at(self):
        """
        test User instances have updated_at attribute
        """
        a = User()
        self.assertTrue(hasattr(a, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
