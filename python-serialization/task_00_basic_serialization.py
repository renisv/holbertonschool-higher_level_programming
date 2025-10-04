#!/usr/bin/env python3

import json
"""module that implements json serialization and deserialization"""


def serialize_and_save_to_file(data, filename):
    """json serialization"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """json deserialization"""
    with open(filename, 'r') as file:
        return json.load(file)
