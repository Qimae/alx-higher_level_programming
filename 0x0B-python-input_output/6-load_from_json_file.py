#!/usr/bin/python3
"""
Module 6-load_from_json_file

Defines function load_from_json_file that
creates an object from a JSON file
"""


def load_from_json_file(filename):
    """creates an object"""
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
