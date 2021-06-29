#!/usr/bin/python3
"""
    Model: file_storage
    dictionary representation to a JSON string
"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """
        Serializes instances to a JSON file and
        deserializes JSON file to instances.
    """
    __file_path =  'file.json'
    __objects = { }

    def all(self):
        """ returns the dictionary __objects """
        return(FileStorage.__objects)

    def new(self,obj):
        """ sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj


    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_dict = {}
        with open(FileStorage.__file_path, "w") as path:#aqui abro el archivo json en modo escritura con un alias paht
            for key, obj in FileStorage.__objects.items():
                json_dict[key] = obj.to_dict()
            my_string = json.dumps(json_dict)
            path.write(my_string)


    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path, "r") as path:
                my_dict = json.load(path)
                for key, value in my_dict.items():
                    if "BaseModel" in key:
                        my_obj = BaseModel(**value)
                    if "User" in key:
                        my_obj = User(**value)
                    self.new(my_obj)
        except:
            pass
