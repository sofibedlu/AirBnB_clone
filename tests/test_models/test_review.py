#!/usr/bin/python3
"""
test module for Review class
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    unittest for Review model class
    """
    def test_review_id(self):
        """
        test Review has id attribute
        """
        a = Review()
        self.assertTrue(hasattr(a, 'id'))

    def test_review_created_at(self):
        """
        test Review instances have created_at attribute
        """
        a = Review()
        self.assertTrue(hasattr(a, 'created_at'))

    def test_Review_updated_at(self):
        """
        test Review instances have updated_at attribute
        """
        a = Review()
        self.assertTrue(hasattr(a, 'updated_at'))


if __name__ == "__main__":
    unittest.main()
