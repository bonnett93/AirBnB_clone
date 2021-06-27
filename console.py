#!/usr/bin/python3
"""Module: console.py"""
import cmd
import json
from os import name
from models.base_model import BaseModel
import models 


class HBNBCommand(cmd.Cmd):
    """"""

    prompt = '(hbnb)'

    def do_create(self, new_obj):
        """asdasdasd"""
       
        if not new_obj:
            print("** class name missing **")
            return
        if new_obj == "BaseModel":
            obj = BaseModel()
            obj.save()
            print(obj.id)
            return
        else:
            print("** class doesn't exist **")
       
    def do_show (self, args):
        args = args.split()
        
        if not args:
            print("** class name missing **")
            return
        name_class = args[0]
        
        if name_class not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        if len(args) > 1:
            obj_id = args[1]
        else:  
            print("** instance id missing **")
            return  
        all_objs = models.storage.all()
        print(obj_id)
        for key,value in all_objs.items():
            print(value)
            if obj_id == value.id:
                print("primer if")
                print(value.__class__.__name__)
                if name_class == value.__class__.__name__:
                    print(value)
                    return
        
        print("** no instance found **")
    
    #def destroy(self, )    
    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """"""
        return
   

if __name__ == '__main__':
    HBNBCommand().cmdloop()
