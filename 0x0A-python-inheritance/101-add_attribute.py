#!/usr/bin/python3
"""create class MyInt"""


def add_attribute(obj, attribute, nattribute):
        """ function that add new attribute if it exists"""
        if not hasattr(obj, "__dict__"):
                raise TypeError("can't add new attribute")
        setattr(obj, attribute, nattribute)
