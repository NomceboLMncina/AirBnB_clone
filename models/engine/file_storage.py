#!/usr/bin/python3
"""Defines the FileStorage class, a simple storage engine for saving and
loading instances of various classes as JSON data.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine.

    Attributes:
        __file_path (str): The path to the file where objects
        are saved as JSON.
        __objects (dict): A dictionary to store all instantiated objects,
                          where keys are formatted as <class name>.<id>.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects containing all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to __objects with a key formatted as
        <class name>.id, allowing it to be saved later.

        Args:
            obj (BaseModel): The object to store in __objects.
        """
        objxname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objxname, obj.id)] = obj

    def save(self):
        """Serializes __objects to a JSON file specified by __file_path.

        Each object is converted to a dictionary representation before saving.
        """
        objd = FileStorage.__objects
        objxdictionary = {obj: objd[obj].to_dict() for obj in objd.keys()}
        with open(FileStorage.__file_path, "w") as f_ile:
            json.dump(objxdictionary, f_ile)

    def reload(self):
        """Deserializes the JSON file specified by __file_path back into
        __objects, if the file exists. Creates new instances of each object.

        This function ignores the operation if the file is not found.
        """
        try:
            with open(FileStorage.__file_path) as f_ile:
                objxdictionary = json.load(f_ile)
                for objc in objxdictionary.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(class_name)(**objc))
        except FileNotFoundError:
            return
