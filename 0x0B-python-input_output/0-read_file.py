#!/usr/bin/python3
""" read file func"""


def read_file(filename=""):
    """ Read a file using `with` statement"""
    with open(filename, 'r') as file:
        print(file.read())
