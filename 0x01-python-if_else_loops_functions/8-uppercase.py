#!/usr/bin/python3
def uppercase(str):
    abc = ""
    for i in str:
        if ord(i) in range(97, 123):
            abc += chr(ord(i) - 32)
        else:
            abc += i
    print(abc)
