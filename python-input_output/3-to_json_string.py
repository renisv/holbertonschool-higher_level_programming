#!/usr/bin/python3
"""module to represent an object as JSON"""
import json

def to_json_string(my_obj):
    """serialize object to JSON"""
    json_string = json.dumps(my_obj)
    return json_string
