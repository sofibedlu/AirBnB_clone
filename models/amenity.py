#!/usr/bin/python3
"""Define the Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """represents Amenity instaneces"""

    name = ''

    def __init__(self, *args, **kwargs):
        """initialize Amenity instances"""
        super().__init__(*args, **kwargs)
