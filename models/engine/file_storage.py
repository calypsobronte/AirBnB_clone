#!/usr/bin/python3
"""
"""
import json
import os


class FileStorage():
    """comment function"""
    __file_path = 'data.json'
    __objects = {}

    def all(self):
        """function comment"""
        return self.__objects

    def new(self, obj):
        """function comment"""
        self.__objects["{}.{}".format(str(type(obj).__name__),
                       str(obj.id))] = obj

    def save(self):
        """function comment"""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}
            json.dump(dict, file)

    def reload(self):
        """ deserialize all the objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        try:
            with open(self.__file_path, "r") as file:
                obj = json.load(file)
            for key, value in obj.values():
                self.__objects[key] = BaseModel(**value)
                self.__objects[key] = User(**value)
                self.__objects[key] = State(**value)
                self.__objects[key] = City(**value)
                self.__objects[key] = Amenity(**value)
        except:
            pass
