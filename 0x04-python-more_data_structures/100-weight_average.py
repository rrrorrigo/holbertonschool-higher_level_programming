#!/usr/bin/python3
def weight_average(my_list=[]):
    r = 0
    d = 0
    if my_list:
        for i, ii in my_list:
            r += i * ii
            d += ii
    result = r / d
    return result
