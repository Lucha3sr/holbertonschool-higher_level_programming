#!/usr/bin/python3

"""This is a class called MyList that inherits from list"""


class MyList(list):

    """Public instance method that prints the list,"""
    """ but sorted (ascending sort)"""

    def print_sorted(self):

        """ all the elements of the list will be of type int"""
        print(sorted(self))
