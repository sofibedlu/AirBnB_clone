#!/usr/bin/python3
"""
test module for base_model module which defines the BaseModel class
"""
import unittest
from models.base_model import BaseModel
import uuid
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
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

    def test_id_attr_two_instances(self):
        """
        check for two instances have different ids
        """
        my_model = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model, my_model2)

    def test_instance_of_created_at_attr(self):
        """
        test instances of 'created_at' attribute
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_updated_at_attr(self):
        """
        test instances of 'updated_at' attribute
        to check its datetime object
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_two_instances_created_at_attr(self):
        """
        test two instances have different created_at attr
        value
        """
        my_model = BaseModel()
        my_model2 = BaseModel()
        self.assertNotEqual(my_model.created_at, my_model2.created_at)

    def test_instances_all_attr(self):
        """
        test for the instances have the minmum attributes
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_rep(self):
        """
        test string rep of the instances is correct
        """
        my_model = BaseModel()
        str_rep = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str_rep, str(my_model))

    def test_new(self):
        """
        test new instances are added to file_storage engine
        when they are created
        """
        my_model = BaseModel()
        objs = storage.all()
        self.assertTrue(my_model in objs.values())

    def test_save_updated_at_attr(self):
        """
        test if the 'save' method updated 'updated_at' attribute
        """
        my_model = BaseModel()
        prev = my_model.updated_at
        my_model.save()
        now = my_model.updated_at
        self.assertNotEqual(prev, now)

    def test__dict_class_name(self):
        """
        test dictionary rep contain instances class name
        with '__class__' key
        """
        my_model = BaseModel()
        self.assertTrue(my_model.to_dict().get('__class__') is not None)

    def test_dict_created_at_attr(self):
        """
        test dictionary rep contains 'created_at' attribute its
        isoformat of datetime object
        """
        my_model = BaseModel()
        to_dict = my_model.to_dict()
        self.assertEqual(to_dict['created_at'],
                         my_model.created_at.isoformat())

    def test_dict_updated_at_attr(self):
        """
        test dictionary rep contains 'updated_at' attr its
        isoformat of datetime object
        """
        my_model = BaseModel()
        to_dict = my_model.to_dict()
        self.assertEqual(my_model.updated_at,
                         datetime.fromisoformat(to_dict['updated_at']))


if __name__ == "__main__":
    unittest.main()
