#!/usr/bin/python3
"""
Module 4-inherits_from
returns true if object is an instance of a class
that inherited(directly or indirectly) otherwise false
"""


def inherits_from(obj, a_class):
    """
    returns true if object is an instance of a class
    that inherited(directly or indirectly) otherwise false

    Attributes:
        obj: object
        a_class: new class
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
