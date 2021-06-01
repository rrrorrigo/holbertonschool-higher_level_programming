#!/usr/bin/python3
""" Mylist class"""


class MyList(list):
    """ Function that print a list"""
    def print_sorted(self):
        l = list(self)
        print(sorted(l))
