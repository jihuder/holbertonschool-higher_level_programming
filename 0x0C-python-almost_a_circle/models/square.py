#!/usr/bin/python3
'''module rectangle'''
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' class Square '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' class constructor of square '''
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' getter of size '''
        return self.width

    @size.setter
    def size(self, value):
        ''' setter of size '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')  # works
        self.width = value

    def __str__(self):
        ''' return a string '''
        s1 = '[Square] ({}) {}/{} -'.format(self.id, self.x, self.y)
        s2 = ' {}'.format(self.width)
        return s1 + s2

    def update(self, *args, **kwargs):
        ''' update the private attributes'''
        vars = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, vars[i], args[i])
        else:
            for i in kwargs.keys():
                if i in dir(self):
                    setattr(self, i, kwargs.get(i))

    def to_dictionary(self):
        ''' returns the dictionary representation of a Square '''
        vars = ['id', 'x', 'size', 'y']
        dictionary = {}
        for i in range(len(vars)):
            dictionary.update({vars[i]: (getattr(self, vars[i]))})
        return dictionary
