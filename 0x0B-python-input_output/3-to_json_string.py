#!/usr/bin/python3
"""
Module 3-to_json_string

Defines function to_json_string that returns JSON representation
of an object
"""


def to_json_string(my_obj):
    """Returns Json representation"""
    import json

    return json.dumps(my_obj)
