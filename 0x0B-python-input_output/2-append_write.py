#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
   and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    add the file and return the number of characters
    """
    with open(filename, 'a') as file:
        nb_char = file.write(text)
        file.close()
        return nb_char
