#!/usr/bin/env python3

"""
Exercise 8.4.
The following functions are all INTENDED to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function,
describe what the function actually does (assuming that the parameter is a string).
"""

def any_lowercase1(s):
    # Checks only first letter in string if it is lowercase or not and returns
    # boolean.
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    # Checks if string 'c' is lowercase or not; and returns string 'True';
    # Returns 'True' everytime, given argument does not matter;
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    # Checks if each letter in string is lowercased or not and assigned the outcome
    # (boolean value) to the variable 'flag'; new value is assigned to 'flag' with
    # every checked letter;
    # Returns boolean value of calling islower() method on only the last letter
    # of the given string;
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    # Checks if there is ANY lowercased letter in given string and returns boolean;
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    # Checks every letter if it is not lowercased and returns boolean if all the
    # letters in string are lowercased or not;
    for c in s:
        if not c.islower():
            return False
    return True
