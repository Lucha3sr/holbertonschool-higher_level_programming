#!/usr/bin/python3

"""function that returns True if the object is an instance of"""
"""or if the object is an instance of a class that inherited from"""
""" otherwise False."""


def inherits_from(obj, a_class):

    """returns True, otherwise False"""
    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
