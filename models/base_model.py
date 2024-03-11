#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    Base class for all models in the AirBnB clone project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, tform))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime and saves the model.
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Converts the model instance to a dictionary representation.

        Returns:
            dict: A dictionary representation of the model instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the model instance.
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
