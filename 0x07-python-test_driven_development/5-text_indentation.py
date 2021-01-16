#!/usr/bin/python3

"""
This Module contains a function that prints a text
with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):

    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if type(text) == str:
        for letter in text:
            if letter == "." or letter == "?" or letter == ":":
                print(letter, end="")
                print("\n")
            elif letter == " ":
                continue
            else:
                print(letter, end="")
    else:
        raise TypeError("text must be a string")
