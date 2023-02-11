#!/usr/bin/python3
"""Define the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """represents Review instances"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """initialize the Review instance with BaseModel"""

        super().__init__(*args, **kwargs)
