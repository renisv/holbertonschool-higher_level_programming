#!/usr/bin/python3
""" (directly or indirectly)"""


def inherits_from(obj, a_class):
    """a class that inherited """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
