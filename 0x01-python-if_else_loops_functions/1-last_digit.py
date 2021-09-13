#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number > 0:
    end = abs(number) % 10
else :
    end = abs(number) % -10
print("Last digit of {:d} is {:d} and is".format(number, end), end=" ")
if end > 5:
    print("greater than 5")
elif end == 0:
    print("0")
elif end < 6:
    print("less than 6 and not 0")
