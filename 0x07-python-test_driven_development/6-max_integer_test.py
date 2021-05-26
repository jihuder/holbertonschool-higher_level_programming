#!/usr/bin/python3
""" Modulo create Function"""


def max_integer(list=[]):
    """Start"""
    if len(list) == 0:
        return None
    largest = list[0]
    i = 1
    while i < len(list):
        if list[i] > largest:
            largest = list[i]
        i += 1
    return largest
