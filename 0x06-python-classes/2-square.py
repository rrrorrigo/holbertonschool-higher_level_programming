#!/usr/bin/python3
""" This is class named Square that defines a square """


class Square:
        """ Definition """
        def __init__(self, size=0):
                """ Initialization of private instance attribute size
                which is asigned with the double underscore before given name

                Args:
                    size (int): private instance attribute.

                Raises:
                    TypeError: if `size` is not an integer
                    ValueError: if `size` is less than zero

                """
                self.__size = size
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                if size < 0:
                        raise ValueError("size must be >=0")
