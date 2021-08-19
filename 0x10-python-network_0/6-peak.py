#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
        """function that finds a peak"""
        l = list_of_integers
        if not l:
                return None
        if len(l) == 1:
                return l[0]
        middle = int(len(l) / 2)
        if l[middle] > l[middle + 1] and l[middle] > l[middle - 1]:
                return l[middle]
        if l[middle] < l[middle + 1] and l[middle] > l[middle - 1]:
                return l[middle + 1]
        else:
                return max(l)
