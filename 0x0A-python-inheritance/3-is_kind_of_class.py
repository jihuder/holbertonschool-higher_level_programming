#!/usr/bin/python3
"""This module if the object is an
        instance or an inherited instance  """


def is_kind_of_class(obj, a_class):
    """ Method to return True if the object is an instance
            or if the object is an instance of a class that
                inherited from the specified class,
                    otherwise False """
    return isinstance(obj, a_class)
