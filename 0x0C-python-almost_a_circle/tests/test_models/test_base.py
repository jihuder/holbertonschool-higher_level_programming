#!/usr/bin/python3
# unit test for base.py script and requirements of the general proyect

import unittest  # allows to assert
import os  # allows to run bash commands

# scripts to test:
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    # class to test the unit models.base.py

    string = 'Betty Holberton'

    def test_base(self):
        # test for class Base, task 0

        a = Base()
        b = Base()
        c = Base()
        d = Base(12)
        e = Base()

        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)
        self.assertEqual(c.id, 3)
        self.assertEqual(d.id, 12)
        self.assertEqual(e.id, 4)

        self.assertTrue(type(a), Base)
        self.assertIsInstance(a, Base)

        # base has a method to_json_string(list_dictionaries)
        # to_json_string devuelve un string

        rect = Rectangle(10, 7, 2, 8)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertTrue(type(dictionary) == dict)
        self.assertTrue(type(json_dictionary) == str)

        # base has a class method save_to_file
        # writes the JSON string representation of a list of objs to a file

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            readed = file.read()

        self.assertTrue(len(readed) > 0)

        s1 = Square(1, 7, 2)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            readed = file.read()

        self.assertTrue(len(readed) > 0)

        os.remove("Rectangle.json")

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            readed = file.read()

        self.assertTrue(readed == '[]')

        os.remove("Rectangle.json")
        os.remove("Square.json")

        # base has a static method from_json_string(json_string)
        # from_json_string devuelve una lista

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertTrue(type(list_input) == list)
        self.assertTrue(type(json_list_input) == str)
        self.assertTrue(type(list_output) == list)

        list_output = Rectangle.from_json_string(None)

        self.assertTrue(type(list_input) == list)
        self.assertTrue(type(json_list_input) == str)
        self.assertTrue(type(list_output) == list)
        self.assertTrue(list_output == [])

        # base has a class method create(cls, **dictionary)
        # returns an object with all the attributes setted

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertTrue(r1.x == r2.x)
        self.assertTrue(r1.y == r2.y)
        self.assertTrue(r1.id == r2.id)
        self.assertTrue(r1.width == r2.width)
        self.assertTrue(r1.height == r2.height)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        # base has a class method load_from_file(cls)
        # returns a list of instances

        # base has a class method save_to_file_csv(cls, list_objs)
        # do

        # base has a class method load_from_file_csv(cls):
        # do

    def doc_of_base(self):
        # documentation of functions

        pass

    def whole_project_requirements(self):
        # existence of all files and directories in the correct location

        self.assertTrue(os.path.isfile('README.md'))

        self.assertTrue(os.path.isdir('models'))

        self.assertTrue(os.path.isfile('./models/__init__.py'))
        self.assertTrue(os.path.isfile('./models/base.py'))
        self.assertTrue(os.path.isfile('./models/rectangle.py'))
        self.assertTrue(os.path.isfile('./models/square.py'))

        self.assertTrue(os.path.isdir('tests'))
        self.assertTrue(os.path.isdir('./tests/test_models'))

        self.assertTrue(os.path.isfile('./tests/test_models/__init__.py'))
        self.assertTrue(os.path.isfile('./tests/test_models/test_base.py'))
        self.assertTrue(os.path.isfile('./tests/test_models/test_rectangle.py'))
        self.assertTrue(os.path.isfile('./tests/test_models/test_square.py'))

        # files are executable
        self.assertTrue(os.access('./models/base.py', os.X_OK))
        self.assertTrue(os.access('./models/rectangle.py', os.X_OK))
        self.assertTrue(os.access('./models/square.py', os.X_OK))

        # first and last line
        with open('./models/base.py') as f:
            first = f.readline()
            last = f.read()[-1]

        self.assertTrue(first == '#!/usr/bin/python3\n')
        self.assertTrue(last == '\n')

        # first and last line rectangle
        with open('./models/rectangle.py') as f:
            first = f.readline()
            last = f.read()[-1]

        self.assertTrue(first == '#!/usr/bin/python3\n')
        self.assertTrue(last == '\n')


        # first and last line square
        with open('./models/square.py') as f:
            first = f.readline()
            last = f.read()[-1]

        self.assertTrue(first == '#!/usr/bin/python3\n')
        self.assertTrue(last == '\n')

        # pep8
        self.assertEqual(os.system('pep8 --count ./models/base.py'), 0)
        self.assertEqual(os.system('pep8 --count ./models/rectangle.py'), 0)
        self.assertEqual(os.system('pep8 --count ./models/square.py'), 0)

        # documentation of modules and classes
        self.assertTrue(len('base'.__doc__) > 8)
        self.assertTrue(len(Base.__doc__) > 8)

        self.assertTrue(len('rectangle'.__doc__) > 8)
        self.assertTrue(len(Rectangle.__doc__) > 8)

        self.assertTrue(len('square'.__doc__) > 8)
        self.assertTrue(len(Square.__doc__) > 8)


if __name__ == '__main__':
    unittest.main()
