#!/usr/bin/python3

"""function that writes a string to a text file (UTF8)"""


def append_write(filename="", text=""):

    """ and returns the number of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
