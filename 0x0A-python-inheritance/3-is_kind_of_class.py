#!/usr/bin/python3
"""
Module 3-is_kind_of_class
return true if object is an instance of,
or is an instance of a class that inherited from the specified class
otherwise false
"""


def is_kind_of_class(obj, a_class):
    """
    return true if object is an instance of,
    or is an instance of a class that inherited from the specified class
    otherwise false

    Attributes:
        obj: object
        a_class: new class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
