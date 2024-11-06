#!/usr/bin/python3
"""
create a sub class that inherits from list
"""


class MyList(list):
    """the class takes the list as argu"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))