#!/usr/bin/python3
"""
Module 5-save_to_json_file

Defines a function that writes an object to
a text file using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to atext file"""
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
