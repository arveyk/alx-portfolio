#!/usr/bin/python3
"""User class
"""
from .base_model import BaseModel

class User(BaseModel):
    """Definition of user class
    """

    def __init__(self):
        super().__init__()
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        
