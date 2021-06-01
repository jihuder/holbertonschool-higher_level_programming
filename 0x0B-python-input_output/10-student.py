#!/usr/bin/python3
"""class Student that defines a student """


class Student:
    """Instantiation class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        """retrieves a dictionary representation of a Student"""

    def to_json(self, attrs=None):
        _dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) == int:
                    _dict = self.__dict__
                try:
                    _dict[i] = getattr(self, i)
                except:
                    pass
        else:
            _dict = self.__dict__
        return (_dict)
