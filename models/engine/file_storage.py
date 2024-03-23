models/engine/file_storage.py

#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place


class FileStorage:
    """Abstracted storage engine Representation"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Dictionary of instantiated objects in __objects returned
        """
        if cl is not None:
            if type(cl) == str:
                cl = eval(cl)
            cl_dict = {}
            for a, b in self.__objects.items():
                if type(b) == cl:
                    cl_dict[a] = b
            return cl_dict
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id."""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """__objects to the JSON file __file_path Serialized"""
        odict = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """if it exists JSON file __file_path to __objects Deserialize"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for a in json.load(f).values():
                    name = a["__class__"]
                    del a["__class__"]
                    self.new(eval(name)(**a))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object if object exists in __objects."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """reload method"""
        self.reload()
