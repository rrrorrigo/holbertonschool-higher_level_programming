#!/usr/bin/python3
""" Class base"""
import json

class Base:
        """ main class called Base"""
        __nb_objects = 0
        def __init__(self, id=None):
                if id is not None:
                        self.id = id
                else:
                        Base.__nb_objects += 1
                        self.id = self.__nb_objects

        def to_json_string(list_dictionaries):
                """ json to string method"""
                if not list_dictionaries:
                        return "[]"
                return json.dumps(list_dictionaries)

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