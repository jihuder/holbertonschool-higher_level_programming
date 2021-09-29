#!/usr/bin/python3
"""class square"""


class Square:
    """start"""
    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            return(self.__size)

        def size(self, value):
            if type(value) is not int:
                raise TypeError('size must be an integer')
            if value < 0:
                raise ValueError('size must be >= 0')

            self.__size = value

        def area(self):
            return(self.__size ** 2)

        def __eq__(self, other):
            return self.size == other.size

        def __ne__(self, other):
            return self.size != other.size

        def __gr__(self, other):
            return self.size > other.size

        def __ge__(self, other):
            return self.size >= other.size

        def __lt__(self, other):
            return self.size < other.size

        def __le__(self, other):
            return self.size <= other.size
