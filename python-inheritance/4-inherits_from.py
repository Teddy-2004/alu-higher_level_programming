#!/usr/bin/python3
"""
only show the instance from inherited class
"""


def inherits_from(obj, a_class):
    """
    returns only for the the inherited class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
