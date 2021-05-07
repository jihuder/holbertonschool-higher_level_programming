#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = []
    for _1 in set_1:
        if _1 not in set_2:
            set_3.append(_1)
    for _2 in set_2:
        if _2 not in set_1:
            set_3.append(_2)
    return set_3
