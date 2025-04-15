#!/usr/bin/python3
"""State class
"""
from base_model import BaseModel


class Place(BaseModel):
    '''email, AI api , entry database'''

    def __init__(self):
        """
        init method"""
        super().__init__()
        self.city_id = ''
        self.user_id = ''
        self.name = ''
        self.description = ''
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.logitude = 0.0
        self.latitude = 0.0
        self.amenity_ids = []
