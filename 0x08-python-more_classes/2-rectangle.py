#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ New Object """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """area method"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.__width + self.__height)
