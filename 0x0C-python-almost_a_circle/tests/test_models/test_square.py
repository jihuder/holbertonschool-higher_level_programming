#!/usr/bin/python3
# unit test for square.py script

import unittest  # allows to assert
import os  # allows to run bash commands

# scripts to test:
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Square(unittest.TestCase):
    # class to test the unit models.rectangle.py

    word = 'Betty'
    string = 'Betty Holberton'
    positive = 5
    negatve = 0 - 5
    zero = 0
    nothing = None
    dictionary = {'Key0': 0, 'Key1': 1, 'Key2': 2, 'Key3': 3, 'Key4': 4}
    list = [1, 2, 3, 4, 5]
    boolean = True

    def test_Square(self):
        # test for class Square

        # Correct input same parameters
        a = Square(100, 100, 100, 100)
        self.assertEqual(a.width, 100)
        self.assertEqual(a.height, 100)
        self.assertEqual(a.size, 100)
        self.assertEqual(a.x, 100)
        self.assertEqual(a.y, 100)
        self.assertEqual(a.id, 100)

        # Rectangle is instance of Base
        self.assertTrue(type(a), Base)
        self.assertIsInstance(a, Base)
        self.assertTrue(type(a), Rectangle)
        self.assertIsInstance(a, Rectangle)

        # Correct input with only mandatory parameters
        c = Square(2)
        self.assertEqual(c.id, 1)
        self.assertEqual(c.width, 2)
        self.assertEqual(c.height, 2)
        self.assertTrue(c.size, 2)
        self.assertEqual(c.x, 0)
        self.assertEqual(c.y, 0)
        Base.id = 0

        # Correct input full parameters
        b = Square(100, 200, 300, 400)
        self.assertEqual(b.size, 100)
        self.assertEqual(b.width, 100)
        self.assertEqual(b.height, 100)
        self.assertEqual(b.x, 200)
        self.assertEqual(b.y, 300)
        self.assertEqual(b.id, 400)

        # Raise error if incorrect Type Value
        # d = Square(string, 3, 4, 5)
        # self.assertRaises(TypeError, d)

    def doc_of_square(self):
        # documentation of square functions
        pass


if __name__ == '__main__':
    unittest.main()
