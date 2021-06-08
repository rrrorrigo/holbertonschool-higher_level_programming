#!/usr/bin/python3
""" Class base"""
import json


class Base:
        """ main class called Base"""
        __nb_objects = 0

        def __init__(self, id=None):
                """ initializer method"""
                if id is not None:
                        self.id = id
                else:
                        Base.__nb_objects += 1
                        self.id = self.__nb_objects

        @staticmethod
        def to_json_string(list_dictionaries):
                """ json to string method"""
                l = list_dictionaries
                if l is not None and len(l) != 0:
                        return json.dumps(l)
                else:
                        return "[]"

        @classmethod
        def save_to_file(cls, list_objs):
                """ write an object to a text file"""
                filename = cls.__name__ + ".json"
                rlist = []
                if list_objs:
                        for x in list_objs:
                                rlist.append(x.to_dictionary())
                with open(filename, 'w', encoding="utf-8") as f:
                        f.write(cls.to_json_string(rlist))

        def from_json_string(json_string):
                """ Return an object representing by json string"""
                return json.loads(json_string) if json_string else []

        @classmethod
        def create(cls, **dictionary):
                """ create a dummy object"""
                aux = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
                aux.update(**dictionary)
                return aux
