#!/usr/bin/python3
import json

"""
dictionary representation to a JSON string
"""

class FileStorage:
    """

    """
    __file_path =  'file.json'# importo el archivo json
    __objects = { } # guardo el valor de la serializacion

    def all(self):
        return(FileStorage.__objects)

    def new(self,obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj


    def save(self):
        """
        """
       # lis = {} # guardo el valor de la serializacion
        #for llave, value in self.__objects.items():# el ciclo cuando itera  con las varibles en dicionario
            #lis[llave] = value #El valor es guardado en un lista para ser la serializacion
        with open(self.__file_path, "w") as path:#aqui abro el archivo json en modo escritura con un alias paht
            for key, obj in FileStorage.__objects.items():
                my_string = json.dumps(obj.to_dict())
                path.write(my_string)
        

    def reload(self):
        """
        """
        from models import BaseModel
        try: #Pongo una exepcion en caso que falle

            with open(FileStorage.__file_path, "r") as path: # abro el archivo en modo lectura y su alias path
                my__dict = json.load(path)
                print("estamos en reload")
                print(my_dict)
                for llave, value in (json.load(paht)).items():#recupero path para del archivo json y lo convierto en un diccionario por lo cual lo recorro como tal
                    my_obj = BaseModel(value)
                    self.new(my_obj)
        
        except:
            pass
        
