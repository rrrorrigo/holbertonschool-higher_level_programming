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

        @property
        def size(self):
                """ size getter method"""
                return self.width

        @size.setter
        def size(self, value):
                """ size setter method"""
                self.width = value
                self.height = value

        def update(self, *args, **kwargs):
                arguments = ["id", "size", "x", "y"]
                if args:
                        for i in range(len(args)):
                                setattr(self, arguments[i], args[i])
                else:
                        for i, ii in kwargs.items():
                                if hasattr(self, i):
                                        setattr(self, i, ii)

        def to_dictionary(self):
                """ dictionary representation method"""
                return {'id': self.id, 'size': self.size,
                        'x': self.x, 'y': self.y}