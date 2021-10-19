#!/usr/bin/python3
'''module rectangle'''
from models.base import Base


class Rectangle(Base):
    ''' class Rectangle '''

    vars = ['id', 'width', 'height', 'x', 'y']

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' class constructor of rectangle '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        ''' getter of width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter of width '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        ''' getter height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter height '''
        if not(isinstance(value, int)):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' getter x '''
        return self.__x

    @x.setter
    def x(self, x):
        ''' setter x '''
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        ''' getter y '''
        return self.__y

    @y.setter
    def y(self, y):
        ''' setter y '''
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        ''' return the area of a rectangle'''
        return(self.__width * self.__height)

    def display(self):
        ''' print rectangle with w, h x and y '''
        if self.area == 0:
            print()
        else:
            for i in range(self.__y):
                print()
            for i in range(self.__height):
                for i in range(self.__x):
                    print(' ', end='')
                for j in range(self.__width):
                    print("#", end='')
                print()

    def __str__(self):
        ''' return a string describing the rectangle properties '''
        s1 = '[Rectangle] ({}) {}/{} -'.format(self.id, self.__x, self.__y)
        s2 = ' {}/{}'.format(self.__width, self.__height)
        return s1 + s2

    def update(self, *args, **kwargs):
        ''' update the private attributes'''
        vars = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, vars[i], args[i])
        else:
            for i in kwargs.keys():
                if i in dir(self):
                    setattr(self, i, kwargs.get(i))

    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        vars = ['x', 'y', 'id', 'height', 'width']
        dictionary = {}
        for i in range(len(vars)):
            dictionary.update({vars[i]: (getattr(self, vars[i]))})
        return dictionary
