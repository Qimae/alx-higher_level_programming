#!/usr/bin/python3
"""
Module 2-append_write

Defines function append_write that appends a string
at the end of a text
"""


def append_write(filename="", text=""):
    """appends a string"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
