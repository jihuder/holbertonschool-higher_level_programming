#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = (0, 0)
        for key, value in a_dictionary.items():
            if best[1] < value:
                best = (key, value)
        return best[0]
