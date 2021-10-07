#!/usr/bin/python3

""" prints a text with 2 new lines after each of these characters: ., ? and """


def text_indentation(text):
    """Prints characters '?' '.' ','"""

    chars = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError('text must be a string')
    for c in range(len(text)):
         if text[c] == ' ' and text[c - 1] in chars:
             continue
         print(text[c], end='')
         if text[c] == '.' or text[c] == '?' or text[c] == ':':
             print('', end='\n\n')
