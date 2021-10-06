#!/usr/bin/python3
"""function that adds two functions"""


def add_integer(a, b=98):
    """add two functions"""
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
