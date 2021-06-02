#!/usr/bin/python3
""" class to json func"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that return a dictionary of object"""
        rd = {}
        if type(attrs) is list:
            for aux in attrs:
                if type(aux) is not str:
                    return self.__dict__
                if aux in self.__dict__:
                    rd[aux] = self.__dict__[aux]
            return rd
        return self.__dict__
