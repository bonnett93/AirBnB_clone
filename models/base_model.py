#!/usr/bin/python3
"""
	Module: models.base_model.py
	BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime




class BaseModel:
   
    """

    """
    def __init__(self, *args, **kwargs):
        from models.__init__ import storage
        """Class constructor"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at","updated_at"]:
                    self.__dict__[key] = datetime.strptime(value,
                                            '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4()) #Getter y Setter???
            self.created_at = datetime.now() #Getter y Setter???
            self.updated_at  = datetime.now() #Getter y Setter???
            storage.new(self)

    def __str__(self):
        """Represents the class objects as a string"""
        msg = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
        return msg

    def save(self):
        from models.__init__ import storage
        """ Updates the public instance attribute updated_at
            with the current datetime """
        self.updated_at  = datetime.now() #Getter y Setter???
        storage.save()
    
    def to_dict(self):
        """ returns a dictionary containing all keys/values of
            __dict__ of the instance """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(
                '%Y-%m-%dT%H:%M:%S.%f')
        return dictionary
