#!/usr/bin/python3
"""
Module 0-read_file

Defines function read_file that reads a file
"""


def read_file(filename=""):
    """opens, reads and prints a file"""
    with open(filename, mode="r", encoding="utf-8") as r:
        print(r.read(), end="")
