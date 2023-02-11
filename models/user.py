#!/usr/bin/python3
"""define the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """ represents User instances """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """initialize the User with Base class"""

        super().__init__(*args, **kwargs)
