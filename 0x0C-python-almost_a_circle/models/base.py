#!/usr/bin/python3
"""
Module base

Defines class Base with private attribute __nb_objects = 0
with class constructor
"""


import json
import csv


class Base():
    """
    Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        objs = []
        if list_objs is not None:
            for i in list_objs:
                objs.append(cls.to_dictionary(i))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            json_string = "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, "r") as f:
                instance = cls.from_json_string(f.read())
            for i, d in enumerate(instance):
                l.append(cls.create(**instance[i]))
        except:
            pass
        return l
