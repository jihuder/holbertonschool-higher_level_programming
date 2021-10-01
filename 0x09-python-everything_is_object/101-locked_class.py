#!/usr/bin/python3
""" Defines a locked class """


class LockedClass:
    """ Avoid creating a new one by the user"""
    __slots__ = ['first_name']
