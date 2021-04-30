#!/usr/bin/python3
i = 122
while(i != 96):
    if i % 2 != 0:
        j = i - 32
    else:
        j = i
    print("{}".format(chr(j)), end="")
    i -= 1
