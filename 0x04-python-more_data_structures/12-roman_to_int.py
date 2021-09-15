#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if isinstance(roman_string, str) and roman_string is not None:
        lenght = len(roman_string)
        for i in range(0, lenght):
            if (i < lenght - 1 and
                    dict.get(roman_string[i]) < dict.get(roman_string[i + 1])):
                integer -= dict.get(roman_string[i])
            else:
                integer += dict.get(roman_string[i])
        return integer
    return 0
