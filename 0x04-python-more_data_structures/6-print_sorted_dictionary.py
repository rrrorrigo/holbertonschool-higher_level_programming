#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for s, s2 in sorted(a_dictionary.items()):
        print("{} : {}".format(s, s2))
