#!/usr/bin/python3
"""State class
"""
from base_model import BaseModel


class Review(BaseModel):
    '''email, AI api , entry database'''
    def __init__(self):
        """
        init method"""
        super().__init__()
        self.place_id = ''
        self.user_id = 0
        self.text = ''
