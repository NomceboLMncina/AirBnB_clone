#!/usr/bin/python3
"""Defines the BaseModel class for the HBnB project, providing essential
attributes and methods for other classes that inherit from it."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base class for all models in the HBnB project.

    Attributes:
        id (str): A unique identifier for each instance, generated with uuid4.
        created_at (datetime): The timestamp when an instance is created.
        updated_at (datetime): The timestamp of the last update to an instance.
"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.
        Args:
            *args (any): Unused positional arguments.
            **kwargs (dict): Key/value pairs of attributes, used for
            Initializing the instance with specific data.
        """
        forma_t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, forma_t)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime
        to mark when changes were last saved, and then saves the instance
        in storage."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the BaseModel instance,
        including its attributes and class name for JSON serialization.

        Returns:
            dict: A dictionary containing all instance attributes.
                  - Includes '__class__' key for the instance's class name.
                  - Converts 'created_at' and 'updated_at' to ISO strings.
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __str__(self):
        """Defines the string representation of the BaseModel instance,
        showing class name, unique ID, and instance's dictionary of attributes.

        Returns:
            str: A formatted string representation of the instance."""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
