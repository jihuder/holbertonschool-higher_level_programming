#!/usr/bin/python3
"""Algorithm must have the lowest complexity"""


def find_peak(list_of_integers):
    """Find whole in a list"""
    lint = list_of_integers
    if lint:
        lint.sort()
        return lint[-1]
    else:
        return None
