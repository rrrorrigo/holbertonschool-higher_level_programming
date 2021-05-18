#!/usr/bin/python3
""" This is class named Square that defines a square """


class Square:
        """ Definition """
        def __init__(self, size):
                """ Initialization of private instance attribute size
                which is asigned with the double underscore before given name

                Args:
                    size (int): private instance attribute.

                """
                self.__size = size
