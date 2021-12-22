#!/usr/bin/python3
"""
Module 1-write_file

Defines function write_file that writes a string to a text file
"""


def write_file(filename="", text=""):
    """writes a string to text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
