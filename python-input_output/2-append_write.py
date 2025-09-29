#!/usr/bin/python3
"""module to append"""


def append_write(filename="", text=""):
    """method to append"""
    with open(filename, 'a', encoding="UTF8") as file:
        character_counter = file.write(text)
        return character_counter
