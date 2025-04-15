#!/usr/bin/python3
"""
Base_model for airbnb clone
"""
from datetime import datetime
import uuid
from . import storage


class BaseModel:
    def __init__(self, *args, **kwargs):

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()   
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            self.created_at = datetime.fromisoformat(kwargs.get("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at"))
            self.id = kwargs.get("id")

    def __str__(self):
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.update_at = str(datetime.now())
        storage.save()
    def to_dict(self):
        """Return the Dictionary representation of object
        Args: none
        Return: dictionary rep
        """
        self.__dict__['__class__']= self.__class__.__name__

        created_at = self.__dict__.get("created_at")
        updated_at = self.__dict__.get("updated_at")

        self.__dict__["created_at"] = str(datetime.isoformat(created_at))
        self.__dict__["updated_at"] = str(datetime.isoformat(updated_at))
        
        return dict(self.__dict__)
