#!/usr/bin/python3
'''module base '''
import json
import os
import time


class Base():
    '''class Base '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''method init'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''static method that returns the JSON string representation of
        list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file '''
        filename = str('{}.json'.format(cls.__name__))
        list_of_dicts = []
        string = '[]'
        if list_objs:
            for obj in list_objs:
                list_of_dicts.append(cls.to_dictionary(obj))
            string = cls.to_json_string(list_of_dicts)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(string)

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string '''
        if json_string is None or len(json_string) < 0:
            return []
        result = json.loads(json_string)
        return result

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if dictionary is None:
            return None
        default = cls(1, 1)
        default.update(**dictionary)
        return default

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances '''
        filename = str('{}.json'.format(cls.__name__))
        exist = os.path.isfile(filename)
        if exist is False:
            return []
        else:
            with open(filename, encoding='utf-8') as file:
                filecontent = file.read()
            list_of_dicts = cls.from_json_string(filecontent)
            list_instances = []
            for dictionary in list_of_dicts:
                object = cls.create(**dictionary)
                list_instances.append(object)
            return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' serializes in CSV '''
        filename = str('{}.csv'.format(cls.__name__))
        list_of_dicts = []
        if list_objs:
            for obj in list_objs:
                list_of_dicts.append(cls.todictionary(obj))
        pass

    @classmethod
    def load_from_file_csv(cls):
        ''' deserializes in CSV '''
        filename = str('{}.json'.format(cls.__name__))
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' opens a window and draws all the Rectangles and Squares '''
        pass
