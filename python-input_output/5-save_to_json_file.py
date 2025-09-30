#!/usr/bin/python3
"""module to save an object to a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """Saves an object to a text file, using a JSON representation.

    Args:
        my_obj (any): The object to be saved.
        filename (str): The name of the file where the object will be saved.
    """
    import json

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
