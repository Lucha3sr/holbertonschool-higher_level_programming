#!/usr/bin/python3

""" import module jason"""
import json

"""function that returns the JSON representation of an object (string"""


def to_json_string(my_obj):

    """You dont need to manage exceptions if the object cant be serialized."""
    return (json.dumps(my_obj))
