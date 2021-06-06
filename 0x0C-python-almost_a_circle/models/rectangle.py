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
                self.__width = value

        @height.setter
        def height(self, value):
                """ setter method of height"""
                self.__height = value

        @x.setter
        def x(self, value):
                """ setter method of x"""
                self.__x = value

        @y.setter
        def y(self, value):
                """ setter method of y"""
                self.__y = value