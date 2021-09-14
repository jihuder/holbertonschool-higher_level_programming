#!/usr/bin/python3
def no_c(my_string):
    nuevo = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            nuevo += i
    return nuevo
