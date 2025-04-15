#!/usr/bin/python3
"""State class
"""
from base_model import BaseModel


class Amenity(BaseModel):
    '''email, AI api , entry database'''


    def __init__(self):
        """
        init method"""
        super().__init__()
        self.name = ''
