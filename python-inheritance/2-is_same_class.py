#!/usr/bin/python3
"""returns True if the object is an instance """


def is_same_class(obj, a_class):
    """an instance of the specified class"""
    if type(obj) is not a_class:
        return False
    return True
