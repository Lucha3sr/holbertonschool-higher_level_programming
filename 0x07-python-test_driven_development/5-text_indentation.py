#!/usr/bin/python3

"""
This Module contains a function that prints a text
with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):

    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    blank_space = 0
    if type(text) == str:
        for letter in text:
            if blank_space == 1:
                blank_space = 0
                continue
            if letter == "." or letter == "?" or letter == ":":
                print(letter, end="")
                print("\n")
                blank_space = 1
            else:
                print(letter, end="")
    else:
        raise TypeError("text must be a string")
