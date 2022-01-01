#!/usr/bin/python3
"""
Module base

Defines class Base with private attribute __nb_objects = 0
with class constructor
"""


class Base():
    """
    Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
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
