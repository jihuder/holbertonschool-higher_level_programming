#!/usr/bin/python3
# unit test for rectangle.py script

import unittest  # allows to assert
import os  # allows to run bash commands

# scripts to test:
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Rectangle(unittest.TestCase):
    # class to test the unit models.rectangle.py

    def test_Rectangle(self):
        # test for class Rectangle, task 0

        # Correct input same parameters
        a = Rectangle(100, 100, 100, 100, 100)
        self.assertEqual(a.width, 100)
        self.assertEqual(a.height, 100)
        self.assertEqual(a.x, 100)
        self.assertEqual(a.y, 100)
        self.assertEqual(a.id, 100)
        Base.id = 0

        # Rectangle is instance of Base
        self.assertTrue(type(a), Base)
        self.assertIsInstance(a, Base)

        # Correct input with only mandatory parameters
        c = Rectangle(2, 3)
        self.assertEqual(c.id, 1)
        self.assertEqual(c.width, 2)
        self.assertEqual(c.height, 3)
        self.assertEqual(c.x, 0)
        self.assertEqual(c.y, 0)
        Base.id = 0

        # Correct input full parameters
        b = Rectangle(100, 200, 300, 400, 500)
        self.assertEqual(b.width, 100)
        self.assertEqual(b.height, 200)
        self.assertEqual(b.x, 300)
        self.assertEqual(b.y, 400)
        self.assertEqual(b.id, 500)

        # Raise error if incorrect Type Value
        # self.assertRaises(TypeError, Rectangle('string', 3, 4, 5))

    def doc_of_rect(self):
        # documentation of rectangle functions

        pass


if __name__ == '__main__':
    unittest.main()
