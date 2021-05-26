#!/usr/bin/python3

""" Module: defines a function that indent text files """


def text_indentation(text):
    """Prints a text with 2 new lines after particular characters"""

    chars = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError('text must be a string')
    for c in range(len(text)):
         if text[c] == ' ' and text[c - 1] in chars:
             continue
         print(text[c], end='')
         if text[c] == '.' or text[c] == '?' or text[c] == ':':
             print('', end='\n\n')
