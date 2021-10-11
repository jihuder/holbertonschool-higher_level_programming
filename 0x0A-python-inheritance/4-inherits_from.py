#!/usr/bin/python3
"""
This module if the object is an
        instance or an inherited instance
"""


def inherits_from(obj, a_class):
    """ Method that returns true or false,
                    if I inherit directly or not.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
