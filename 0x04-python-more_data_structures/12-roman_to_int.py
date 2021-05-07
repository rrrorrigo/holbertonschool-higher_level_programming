#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if roman_string and isinstance(roman_string, str):
        c = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i, ii in enumerate(roman_string):
            if len(roman_string) == i + 1 or c[ii] >= c[roman_string[i + 1]]:
                result += c[ii]
            else:
                result -= c[ii]
    return result
