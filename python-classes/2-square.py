#!/usr/bin/python3
"""private instant attribute with exceptions"""


class Square:
    """class raises an error"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = size
