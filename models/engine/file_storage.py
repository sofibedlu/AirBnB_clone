#!/usr/bin/python3
""" define the class FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ serializes instances to JSON file and deserializes
        JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the 'obj' with key '<obj class name>.id'
        """

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file specified by __file_path
        """

        dict_rep = {}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            for key, value in FileStorage.__objects.items():
                dict_rep[key] = value.to_dict()
            json.dump(dict_rep, f)

    def reload(self):
        """deserializes the JSON file to __objects if the file exist
            if the file doesn't exit, no exception raised
        """

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                for value in json.load(f).values():
                    self.new(eval(value['__class__'])(**value))
        except FileNotFoundError:
            return
