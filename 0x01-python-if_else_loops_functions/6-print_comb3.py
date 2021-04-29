#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != j) and (i < j):
            if (i == 8) and (j == 9):
                print("{}".format(i), end="")
                print("{}".format(j))
            else:
                print("{}".format(i), end="")
                print("{}".format(j), end=", ")
