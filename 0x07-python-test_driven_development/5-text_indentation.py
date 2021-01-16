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
    space_case = 0
    for char in text:
        if space_case == 0:
            if char == " ":
                continue
            else:
                print(char, end="")
                space_case = 1
        else:
            if char == "?" or char == "." or char == ":":
                print(char)
                print("")
                space_case = 0
            else:
                print(char, end="")
