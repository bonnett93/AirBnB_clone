#!/usr/bin/python3
"""
    This module contains test cases for amenity.py
"""
import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """" Unitest cases for Amenity class """
    def setUp(self) -> None:
        super().setUp()
        self.obj = Amenity()
        self.obj2 = Amenity()

    def testAmenityInstance(self):
        '''Check instance creation and attributes'''
        # Check id
        self.assertIs(type(obj.id), str)
        # Check created_at
        self.assertIs(type(obj.created_at), datetime)
        # Check updated_at
        self.assertIs(type(obj.updated_at), datetime)

        # Check new arguments
        self.assertEqual(obj.width, 5)
        # Check x
        self.assertEqual(obj.x, 0)
        # Check y
        self.assertEqual(obj.y, 0)

        # New instance, all arguments
        r2 = Rectangle(5, 5, 5, 5, 5)
        # Check height
        self.assertEqual(r2.height, 5)
        # Check width
        self.assertEqual(r2.width, 5)
        # Check x
        self.assertEqual(r2.x, 5)
        # Check y
        self.assertEqual(r2.y, 5)
        # Check id
        self.assertEqual(r2.id, 5)

    def testRectangleErrors(self):
        '''Check wrong instance creation and attributes'''
        # No arguments
        with self.assertRaises(TypeError):
            r = Rectangle()
        # Wrong type argument height
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")
        # Wrong value argument Width
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        # Wrong type argument x
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        # Wrong value argument y
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)

    def test_area(self):
        '''Check instance method area()'''
        obj = Rectangle(3, 2)
        self.assertEqual(obj.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        with self.assertRaises(TypeError):
            r3.area(8)

    def test_display(self):
        '''Check instance method display()'''
        # with No arguments
        obj = Rectangle(4, 3)
        self.assertEqual(obj.display(), None)

        with self.assertRaises(TypeError):
            obj.display(4)

    def test_str(self):
        '''Check instance method str'''
        obj = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(obj), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        '''Check instance method update'''
        obj = Rectangle(10, 10, 10, 10)
        # No arguments
        obj.update()
        self.assertEqual(str(obj), "[Rectangle] (1) 10/10 - 10/10")
        # one argument
        obj.update(89)
        self.assertEqual(str(obj), "[Rectangle] (89) 10/10 - 10/10")
        # two arguments
        obj.update(89, 2)
        self.assertEqual(str(obj), "[Rectangle] (89) 10/10 - 2/10")
        # three arguments
        obj.update(89, 2, 3)
        self.assertEqual(str(obj), "[Rectangle] (89) 10/10 - 2/3")
        # four arguments
        obj.update(89, 2, 3, 4)
        self.assertEqual(str(obj), "[Rectangle] (89) 4/10 - 2/3")
        # five arguments
        obj.update(89, 2, 3, 4, 5)
        self.assertEqual(str(obj), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        '''Check instance method update'''
        obj = Rectangle(10, 10, 10, 10, 10)
        # No arguments
        obj.update()
        self.assertEqual(str(obj), "[Rectangle] (10) 10/10 - 10/10")
        # if args existx, ignore kwargs
        obj.update(90, height=1)
        self.assertEqual(str(obj), "[Rectangle] (90) 10/10 - 10/10")
        # one argument
        obj.update(height=1)
        self.assertEqual(str(obj), "[Rectangle] (90) 10/10 - 10/1")
        # two arguments
        obj.update(width=1, x=2)
        self.assertEqual(str(obj), "[Rectangle] (90) 2/10 - 1/1")
        # more arguments
        obj.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(obj), "[Rectangle] (89) 3/1 - 2/1")
        # and more
        obj.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(obj), "[Rectangle] (89) 1/3 - 4/2")
        # Type Error
        with self.assertRaises(TypeError):
            obj.update(x="12")
        # value error
        with self.assertRaises(ValueError):
            obj.update(width=-12)
