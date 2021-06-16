#!/usr/bin/python3
"""create class MyInt"""


class MyInt(int):
        """ class Myint that swap == with !="""
        def __eq__(self, other):
                """ swap == with !="""
                return int.__ne__(self, other)

        def __ne__(self, other):
                """ swap != with =="""
                return int.__eq__(self, other)