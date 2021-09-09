#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ultimo = abs(number) % 10

if number < 0:
    ultimo = -ultimo

print("Last digit of {} is {} and is".format(number, ultimo), end=" ")
if ultimo == 0:
    print("and is 0")
elif ultimo > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
