#!/usr/bin/python3
"""module to write a file"""


def write_file(filename="", text=""):
    """writes a file"""
    with open(filename, 'w', encoding="UTF8") as file:
        character_counter = file.write(text)
        return character_counter
