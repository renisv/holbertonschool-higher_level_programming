#!/usr/bin/python3
import json
"""module to represent an object as JSON"""


def to_json_string(my_obj):
    """serialize object to JSON"""
    json_string = json.dumps(my_obj)
    return json_string
