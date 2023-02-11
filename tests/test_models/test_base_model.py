#!/usr/bin/python3
"""
test module for base_model module which defines the BaseModel class
"""
import unittest
from models.base_model import BaseModel
import uuid


class TestBaseModel_init(unittest.TestCase):
    """unittest for constructor method of BaseModel class
    """

    def test_id_attr_no_args(self):
        """
        test the id attribute of the object when
        no args passed
        """
        my_model = BaseModel()
        uuid_obj = uuid.UUID(my_model.id)
        self.assertIsInstance(uuid_obj, uuid.UUID)


if __name__ == "__main__":
    unittest.main()
