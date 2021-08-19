#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
        """function that finds a peak"""
        l = list_of_integers
        if l and l.count(l[0]) == len(l):
                return l[0]
        for i in range(1, len(list_of_integers) - 1):
                if l[i] > l[i - 1] and l[i] > l[i + 1]:
                        return l[i]
