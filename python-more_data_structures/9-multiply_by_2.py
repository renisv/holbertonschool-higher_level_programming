#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    doubled_dictionary = {}
    for key, value in a_dictionary:
        doubled_dictionary.update(key, value * 2)
    return doubled_dictionary