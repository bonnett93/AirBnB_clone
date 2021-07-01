#!/usr/bin/python3
"""
    This module contains test cases for amenity.py
"""
import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel  
from models.engine.file_storage import FileStorage
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
    
class Test_File_storage(unittest.TestCase):
    
    """" Unitest cases for Amenity class """
    