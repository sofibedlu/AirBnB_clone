#!/usr/bin/python3
"""
test module for FileStorage class in file_storage module
"""

import uuid
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    unittest for FileStorage class
    """

    def test_file_path_attr(self):
        """
        check the private class attribute __file_path
        """
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.__file_path
        with self.assertRaises(AttributeError):
            fs.file_path

    def test_objects_attr(self):
        """
        check 'objects' is private class attribute
        """
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.__objects

    def test_all_method_type(self):
        """
        test the type all() method return is dictionary
        """
        fs = FileStorage()
        self.assertTrue(type(fs.all()) is dict)

    def test_all_method(self):
        """
        test the method all returns the dictionary of the instances
        from the private class attribute __objects
        """
        b = BaseModel()
        fs = FileStorage()
        self.assertTrue(b in fs.all().values())


if __name__ == "__main__":
    unittest.main()
