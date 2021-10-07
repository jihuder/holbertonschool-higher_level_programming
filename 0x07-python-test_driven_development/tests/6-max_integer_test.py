#!/usr/bin/python3

""" Unittesting for 6-max_integer.py """

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Methods to test the module """

    def test_possitive(self):
        self.assertEqual(max_integer([10, 20, 30, 40]), 40)
        self.assertEqual(max_integer([77, 66, 55, 44]), 77)
        self.assertEqual(max_integer([1, 2, 3, 88, 0]), 88)

    def test_negative(self):
        l = [-88, -48, -13, -3]
        self.assertEqual(max_integer(l), -3)

    def test_one_arg(self):
        l = [23]
        self.assertEqual(max_integer(l), 23)

    def test_empty(self):
        l = []
        self.assertEqual(max_integer(l), None)

    def test_floats(self):
        l = [1.1, 2.2, 3.3, 7.7]
        self.assertEqual(max_integer(l), 7.7)

    def test_double_max(self):
        l = [89, 33, 45, 60, 89]
        self.assertEqual(max_integer(l), 89)

    def test_string(self):
        l = "string"
        self.assertEqual(max_integer(l), 't')

    def test_mixed_list(self):
        l = ['Y', 3, 6.9]
        with self.assertRaises(TypeError):
             max_integer(l)

if __name__ == '__main__':
    unittest.main()
