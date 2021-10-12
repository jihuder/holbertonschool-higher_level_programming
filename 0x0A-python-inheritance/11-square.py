#!/usr/bin/python3
"""
In this module we start
    building the Square class from
                inherintance Rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle """

    def __init__(self, size):
        """ method init a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method returns the area"""
        return super().area()

    def __str__(self):
            """Method that returns a string from
                    the inheritance of the string string """
            return "[Square] {}/{}".format(self.__size, self.__size)
