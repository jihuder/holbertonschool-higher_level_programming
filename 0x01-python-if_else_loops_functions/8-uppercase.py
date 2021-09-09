#!/usr/bin/python3
def uppercase(str):
    literal = ""
    for i in str:
        if ord(i) in range(97, 123):
            literal += chr(ord(i) - 32)
            print("", end="")
        else:
            literal += i
    print("{}".format(literal))
