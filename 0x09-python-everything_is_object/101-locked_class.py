#!/usr/bin/python3
""" locked class"""


class LockedClass():
        """ class without attribute and only can add first_name as attribute"""
        __slots__ = ['first_name']
