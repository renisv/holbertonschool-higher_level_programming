#!/usr/bin/python3

def roman_to_int(roman_string):
    if len(roman_string) == 0 or roman_string == None:
        return None
    roman_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    number = 0
    for i in range(len(roman_string)):
        current_value = roman_dict[roman_string[i]]
        if i + 1 < len(roman_string):
            next_value = roman_dict[roman_string[i + 1]]
            if current_value < next_value:
                number -= current_value
            else:
                number += current_value
        else:
            number += current_value
    return number
