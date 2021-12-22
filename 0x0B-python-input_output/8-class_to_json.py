#!/usr/bin/python3
"""
Module 8-class_to_json

Defines function class_to_json that returns the dictionary
description with simple data structures
"""


def class_to_json(obj):
    """returns dictionary description"""
    return obj.__dict__
