#!/usr/bin/python3

'''

Module to print a given text
and insterting newlines when encountaring
this type of characters . ? !
'''


def text_indentation(text):
    '''

    Function that prints the text given as argument
    and inserting newlines when encountaring this
    type of characters . ? !
    '''

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print("\n\n", end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
