#!/usr/bin/python3
"""
 MyList class that
        inherits from list
"""


class MyList(list):
    """ Class MyList that inherits
            form list"""
    def print_sorted(self):
        """ Public instance
                method printing list """
        list = sorted(self)
        print(list)
