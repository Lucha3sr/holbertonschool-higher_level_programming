#!/usr/bin/python3

""" function that returns True if the object is exactly an instance"""
""" of the specified class ; otherwise False."""


def is_same_class(obj, a_class):

    """ returns True if the object is exactly an instance of the class"""
    """ otherwise returns False"""
    if type(obj) == a_class:
        return True
    else:
        return False
