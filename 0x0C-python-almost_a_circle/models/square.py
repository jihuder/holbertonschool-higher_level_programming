#!/usr/bin/python3
"""In this module we start to
        create the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialized the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))

    @property
    def size(self):
        """Methodo GET: property Getter return Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Methodo SET: Setter the Square
        """
        self.width = value
        self.heigth = value

    def update(self, *args, **kwargs):
        """Method that update square"""
        dict_order = ['id', 'size', 'x', 'y']
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
        """Method that returns the dictionary Square """
        dict_order = ['id', 'x', 'size', 'y']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
