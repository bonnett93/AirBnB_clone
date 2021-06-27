#!/usr/bin/python3
"""
dictionary representation to a JSON string
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """

    """
    __file_path =  'file.json'# importo el archivo json
    __objects = { } # guardo el valor de la serializacion

    def all(self):
        """"""
        return(FileStorage.__objects)

    def new(self,obj):
        """"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj


    def save(self):
        """
        """
        json_dict = {}
        with open(self.__file_path, "w") as path:#aqui abro el archivo json en modo escritura con un alias paht
            for key, obj in FileStorage.__objects.items():
                json_dict[key] = obj.to_dict()
            my_string = json.dumps(json_dict)
            path.write(my_string)


    def reload(self):
        """
        """
        try:
            with open(FileStorage.__file_path, "r") as path:
                my_dict = json.load(path)
                for llave, value in my_dict.items():
                    my_obj = BaseModel(value)
                    self.new(my_obj)
        except:
            pass

