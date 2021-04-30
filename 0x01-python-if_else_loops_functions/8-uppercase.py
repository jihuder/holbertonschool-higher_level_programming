#!/usr/bin/python3
def uppercase(str):
    copy = ""
    for i in str:
        if ord(i) in range(97, 123):
            copy += chr(ord(i) - 32)
        else:
            copy += i
    print(copy, end="")
    print()
