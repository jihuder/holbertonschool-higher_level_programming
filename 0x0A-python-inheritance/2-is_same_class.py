#!/usr/bin/python3
"""
In this module we make it return
        False or True depending on the object
"""


def is_same_class(obj, a_class):
    """
    Method to return Truesi If the object is
    exactly an instance of the specified class,
    otherwise False
    """
    return type(obj) == a_class
