#!/usr/bin/python3

"""define the BaseModel class
    for each instances create using Base class BaseModel will
    automatically assigned to unique uuid and the time when the
    instance created...and also provide different function to
    manipulate the instances
"""
import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes
        and represents BaseModel instances
    """

    def __init__(self, *args, **kwargs):
        """initialize the instances"""
        from models import storage

        if bool(kwargs):
            for key in kwargs.keys():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                elif key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string representation of an object"""

        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id,
                                       self.__dict__)
        return string

    def save(self):
        """updates the public instance attribute updated_at
            with current datetime
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns dictionary representation of the instance
        """

        s_dict = self.__dict__.copy()
        s_dict['__class__'] = self.__class__.__name__
        s_dict['created_at'] = self.created_at.isoformat()
        s_dict['updated_at'] = self.updated_at.isoformat()
        return s_dict
