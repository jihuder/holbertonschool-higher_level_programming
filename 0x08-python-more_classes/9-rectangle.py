#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ New Object """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """str method"""
        cadena = ""
        if self.height == 0 or self.width == 0:
            return cadena
        for i in range(self.height):
            for j in range(self.width):
                cadena += str(self.print_symbol)
            if self.height - 1 != i:
                cadena += "\n"
        return cadena

    def __repr__(self):
        """repr method"""
        var = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return var

    def __del__(self):
        """del method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """biigger_or_equal """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
