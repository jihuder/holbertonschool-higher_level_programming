#!/usr/bin/python3
def uniq_add(my_list=[]):
    only_1 = set(my_list)
    add = 0
    for i in only_1:
        add += i
    return add
