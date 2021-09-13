#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number > 0:
    end = abs(number) % 10
else :
    end = abs(number) % -10
print("Last digit of {:} is {:}".format(number, end), end=" ")
if end > 5:
    print("and is greater than 5")
elif end == 0:
    print("and is 0")
elif end < 6:
    print("and is less than 6 and not 0")
