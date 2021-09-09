#!/usr/bin/python3
def print_last_digit(number):
    ultimo = abs(number) % 10
    print("{}".format(ultimo), end="")
    return(ultimo)
