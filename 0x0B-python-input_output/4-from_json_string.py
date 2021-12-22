#!/usr/bin/python3
"""
Module 4-from_json_string

Defines functions from_json_string that returns an object
represented by a JSON string
"""


def from_json_string(my_str):
    """returns an object"""
    import json

    return json.loads(my_str)
