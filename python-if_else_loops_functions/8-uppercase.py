#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print("{}".format(result))
