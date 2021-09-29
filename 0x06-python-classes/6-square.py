#!/usr/bin/python3
"""class square"""


class Square:
    """start"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """The area of aquare"""
    def area(self):
        return(self.__size ** 2)

    """Print Square"""
    def my_print(self):
        if self.size == 0:
            print('')
            return
        if self.position[1] > 0:
            for i in range(self.position[1]):
                print('')
        for j in range(self.size):
            print(" " * self.position[0], end='')
            print('#' * self.size, end='')
            print('')
