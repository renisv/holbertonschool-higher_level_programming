#!/usr/bin/env python3

import json
"""module that implements json serialization and deserialization"""


def serialize_and_save_to_file(data, filename):
    """json serialization"""
    try:
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(data, file)
    except FileNotFoundError:
        print(f"{filename} not found")


def load_and_deserialize(filename):
    """json deserialization"""
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            python_object = json.load(file)
            return python_object
    except FileNotFoundError:
        print(f"{filename} not found")
        return {}
