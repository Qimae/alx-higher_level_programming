#!/usr/bin/python3
"""
Module 2-is_same_class
returns true if same instance otherwise false
"""


def is_same_class(obj, a_class):
    """
    Returns true if same instance false otherwise

    Attributes:
        obj: object
        a_class: new class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
