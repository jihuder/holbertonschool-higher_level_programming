#!/usr/bin/python3

""" Module: defines a function that prints name with first and last name """

def say_my_name(first_name, last_name=""):
    """Prints names """
if type(first_name) is not str:
    raise TypeError('firs_name must be a string')
if type(last_name) is not str:
    raise TypeError('last_name must be a string')

print('My name is {} {}'.format(first_name, last_name))
