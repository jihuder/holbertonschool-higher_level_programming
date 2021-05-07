#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = []
    for _1 in set_1:
        for _2 in set_2:
            if _1 == _2:
                set_3.append(_1)
    return set_3
