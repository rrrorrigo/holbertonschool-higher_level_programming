#!/usr/bin/python3
""" Class base"""
from base import Base

class Rectangle(Base):
        """ class Rectangle inherits from Base"""
        def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        @property
        def width(self):
                """ getter method of width"""
                return self.__width

        @property
        def height(self):
                """ getter method of height"""
                return self.__height

        @property
        def x(self):
                """ getter method of x"""
                return self.__x

        @property
        def y(self):
                """ getter method of y"""
                return self.__y

        @width.setter
        def width(self, value):
                """ setter method of width"""
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                if value <= 0:
                        raise ValueError("width must be > 0")
                self.__width = value

        @height.setter
        def height(self, value):
                """ setter method of height"""
                if type(value) is not int:
                        raise TypeError("height must be an integer")
                if value <= 0:
                        raise ValueError("height must be > 0")
                self.__height = value

        @x.setter
        def x(self, value):
                """ setter method of x"""
                if type(value) is not int:
                        raise TypeError("x must be an integer")
                if value < 0:
                        raise ValueError("x must be >= 0")
                self.__x = value

        @y.setter
        def y(self, value):
                """ setter method of y"""
                if type(value) is not int:
                        raise TypeError("y must be an integer")
                if value < 0:
                        raise ValueError("y must be >= 0")
                self.__y = value

        def area(self):
                """ return the area of the rectangle"""
                return self.__height * self.__width

        def display(self):
                """ print in stdout the Rectangle"""
                y = self.__width
                x = self.__height
                for i in range(x):
                        for i in range(y):
                                print('#', end="")
                        print("")