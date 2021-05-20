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

    def area(self):
        return(self.__size ** 2)

    def my_print(self):
        if self.__size != 0:

            for k in range(self.__position[1]):
                print()
            for l in range(self.__size):
                for i in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print('')
        else:
            print('')
