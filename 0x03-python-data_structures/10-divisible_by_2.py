#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lista = list(" " * len(my_list))
    i = 0
    for ele in my_list:
        if ele % 2 == 0:
            lista[i] = True
        else:
            lista[i] = False
        i += 1
    return lista
