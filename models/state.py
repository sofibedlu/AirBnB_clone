#!/usr/bin/python3
""" Define the State class """
from models.base_model import BaseModel


class State(BaseModel):
    """ represents State instances """

    name = ''

    def __init__(self, *args, **kwargs):
        """ initialize the the State instances with the Base class """
        super().__init__(*args, **kwargs)
