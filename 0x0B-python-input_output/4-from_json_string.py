#!/usr/bin/python3

""" import module jason"""
import json

"""function that returns an object represented by a JSON string"""


def from_json_string(my_str):

    """You dont need to manage exceptions if the JSON string"""
    """doesnt represent an object."""

    return (json.loads(my_str))
