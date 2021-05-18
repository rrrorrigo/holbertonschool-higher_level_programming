#!/usr/bin/python3
""" This is class named Square that defines a square """


class Square():
        """ definition """
        def __init__(self, size=0):
                """ Definition of private instance attribute size which
                is asigned with the double underscore before the name

                Args:
                    size (int): private instance attribute.

                Raises:
                    TypeError: if `size` is not an integer
                    ValueError: if `size` is less than zero

                """
                if type(size) is not int:
                        raise TypeError("size must be an integer")
                elif size < 0:
                        raise ValueError("size must be >= 0")
                else:
                        self.__size = size
