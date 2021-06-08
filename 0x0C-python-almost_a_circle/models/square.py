#!/usr/bin/python3
""" Class square"""
from rectangle import Rectangle

class Square(Rectangle):
        """ class square with init method"""
        def __init__(self, size, x=0, y=0, id=None):
                super().__init__(size, size, x, y, id)
                self.size = size

        def __str__(self):
            """ string representation"""
            msg = "[Square] ({}) {}".format(self.id, self.x)
            return msg + "/{} - {}".format(self.y, self.size)