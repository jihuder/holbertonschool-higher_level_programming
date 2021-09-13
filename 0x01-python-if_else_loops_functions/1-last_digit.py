#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number > 0:
    end = number % 10
else :
    end = number % -10
print("Last digit of {:d} is {:d} ".format(number, end), end=" ")
if end > 5:
    message = "and is greater than 5"
elif end == 0:
    message = "and is 0"
elif end < 6:
    message = "and is less than 6 and not 0"
print(message)
