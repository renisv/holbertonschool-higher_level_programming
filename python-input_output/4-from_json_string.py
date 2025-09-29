#!/usr/bin/python3
"""module to represent a JSON string to pythonic object"""
import json


def from_json_string(my_str):
    """returns pythonic object"""
    python_object = json.loads(my_str)
    return python_object
