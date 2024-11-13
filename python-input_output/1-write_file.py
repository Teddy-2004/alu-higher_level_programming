#!/usr/bin/python3
"""
Program that counts lines in a file
"""


def write_file(filename="", text=""):
    """
    count lines in file
    """
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        linenum = f.write(text)
        return linenum
