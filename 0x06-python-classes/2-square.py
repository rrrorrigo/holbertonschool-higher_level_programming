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
                try:
                        if size >= 0:
                                self.__size=size
                        else:
                                raise ValueError("size must be >=0")
                except TypeError:
                        raise TypeError("size must be an integer")
