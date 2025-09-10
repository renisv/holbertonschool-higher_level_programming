#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    doubled_dictionary = a_dictionary.copy()
    for key, value in doubled_dictionary.items():
        doubled_dictionary[key] = value * 2
    return doubled_dictionary
