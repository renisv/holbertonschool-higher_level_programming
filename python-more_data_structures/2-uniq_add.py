#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_of_digits = 0
    firstly_set = set(my_list)
    secondly_list = list(firstly_set)
    for digit in secondly_list:
        sum_of_digits += digit
    return sum_of_digits
