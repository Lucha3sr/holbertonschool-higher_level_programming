#!/usr/bin/python3

"""Write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):

    """You must use the with statement"""
    """You dont need to manage file permission"""
    """or file doesn't exist exceptions."""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
