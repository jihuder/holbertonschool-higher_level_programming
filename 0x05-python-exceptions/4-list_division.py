#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    transladar = []
    for i in range(list_length):
        try:
            contenido = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            contenido = 0
            print("division by 0")
            continue
        except TypeError:
            contenido = 0
            print("wrong type")
            continue
        except IndexError:
            contenido = 0
            print("out of range")
            continue
        finally:
            transladar += [contenido]
        return(transladar)
