#!/usr/bin/python3

"""

function that adds 2 integers

"""

def add_integer(a, b=98):

    """ a and b must be integers or floats
    a and b must be first casted to integers if they are float
    returns an integer: the addition of a and b """


    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    # cast float to int

    a = int(a)
    b = int(b)

    return a + b
