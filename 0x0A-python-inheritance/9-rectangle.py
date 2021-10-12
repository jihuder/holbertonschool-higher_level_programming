#!/usr/bin/python3
"""
In this module we start building
    the rectangle class from inherintance
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry """

    def __init__(self, width, height):
        """ method init a object """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ method returns area """
        return (self.__width * self.__height)

    def __str__(self):
        """ method returns a string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
