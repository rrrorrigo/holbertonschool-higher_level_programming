#!/usr/bin/python3
def multiply_by_2(a_dictionary):
        dictionary = a_dictionary.copy()
        for i, s in dictionary.items():
                dictionary[i] = s * 2
        return dictionary
