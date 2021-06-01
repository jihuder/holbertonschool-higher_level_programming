#!/usr/bin/python3
"""
writes a string to a text file (UTF8) and returns the number of characters
"""


def write_file(filename="", text=""):
    """function that returns the typed characters"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return(file.write(text))
