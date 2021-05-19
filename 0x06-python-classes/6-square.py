#!/usr/bin/python3
""" This is class named Square that defines a square """


class Square:
        """ definition """
        def __init__(self, size=0, position=(0, 0)):
                """ Definition of private instance attribute size
                which is asigned with the double underscore before the name

                Args:
                    size (int): private instance attribute.
                    position (int, int): private instance attribute.

                Raises:
                    TypeError: if `size` is not an integer
                    ValueError: if `size` is less than zero

                """
                self.size = size
                self.position = position

        @property
        def size(self):
                """ getter function"""
                return self.__size

        @property
        def position(self):
            """ definition of function that return the value"""
                return self.__position

        @size.setter
        def size(self, value):
                """ setter func """
                if type(value) is not int:
                        raise TypeError("size must be an integer")
                elif value < 0:
                        raise ValueError("size must be >=0")
                else:
                        self.__size = value

        @position.setter
        def position(self, value):
            """ definition of function that set the value"""
            if type(value) is not tuple or len(value) is not 2 or \
               type(value[0]) is not int or value[0] < 0 or \
               type(value[1]) is not int or value[1] < 0:
                    raise TypeError("position must be a tuple of\
 2 positive integers")
            else:
                    self.__position = value

        def area(self):
                """ Definition of function area that calculate
                the area of the square"""
                return self.__size ** 2

        def my_print(self):
                """ Definition of function that print the area of square"""
                i = self.__size
                position1 = self.position[1]
                position2 = self.position[0]

                if i == 0:
                        print("")
                else:
                        for spaces in range(position1):
                                print("")
                        for x in range(i):
                                print(" " * self.position[0], end="")
                                for y in range(0, i):
                                        print("#", end="")
                                print("")
