#!/usr/bin/python3
"""Define the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """represents City instances"""

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """initialize the instances with the BaseModel class"""
        super().__init__(*args, **kwargs)
