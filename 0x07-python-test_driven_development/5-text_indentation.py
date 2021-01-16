#!/usr/bin/python3

"""
This Module contains a function that prints a text
with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):

    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    blank_space = 0
    for char in text:
        if blank_space == 0:
            if char == " ":
                continue
            else:
                print(char, end="")
                blank_space = 1
        else:
            if char == "?" or char == "." or char == ":":
                print(char, end="")
                print("\n")
                blank_space = 0
            else:
                print(char, end="")
