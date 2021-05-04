#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for i in matrix:
                # string.join(iterable) that iterable is the tuple to print
                # and string is the separator to print
                print(" ".join("{:d}".format(n) for n in i))
