#!/usr/bin/python3
"""
We start defining
    the class geometry, area
            and integer_validator
"""


class BaseGeometry:
    """ Class Basegeometry """

    def area(self):
        """ This method generates an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This method Validates the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".
                             format(name))
