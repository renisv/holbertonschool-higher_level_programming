#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum_of_digits = 0
    make_a_set = set(my_list)
    for digit in make_a_set:
        sum_of_digits += digit
    return sum_of_digits
