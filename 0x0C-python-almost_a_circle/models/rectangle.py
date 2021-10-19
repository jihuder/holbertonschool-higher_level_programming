#!/usr/bin/python3
"""This is the module of the rectangle class"""
from models.base import Base

class Rentagle(Base):
    """This is a Class rectangle"""
def __init__(self, width, height, x=0, y=0, id=None):
    """Rectangle constructor method"""
    self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Getter and setter of width
    @property
    def width(self):
        """Methodo GET: property Getter return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Methodo SET: Setter the whidth"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # The height of the class
    @property
    def height(self):
        """Methodo GET: Property Getter return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Methodo SET: Setter the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # The variable x of the class
    @property
    def x(self):
        """Methodo GET: Property Getter return __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Methodo SET: Setter the height"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # The variable y  of the class
    @property
    def y(self):
        """Methodo GET: Property Getter return __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Methodo SET: Setter the height"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Method for calculating the area of the retangle"""
        return self.width * self.height

    def display(self):
        """Method that prints Rectangle"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + self.width * '#')

    def __str__(self):
        """Method that override str method"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Method for calculating the area of the retangle"""
        dict_order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method that returns the
                    object in the form of a dictionary.
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
