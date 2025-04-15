#!/usr/bin/python3
"""File Storage"""
import json
import os


class FileStorage:
    """ file storage class
    """
    __file_path = "./file.json"
    __objects = {}

    def __init__(self):
        """Init method
        """
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[obj_key] = obj.to_dict()

    def save(self):
        """Saves , serialixes __objects
        Args: None
        Returns
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserialize
        """
        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path) > 0:
                with open(self.__file_path, 'r') as f:
                    d = json.load(f)
                    self.__objects = d
