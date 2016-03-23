#!/usr/bin/env python3

"""
Exercise 11.4.
If you did Exercise 10.7, you already have a function named has_duplicates
that takes a list as a parameter and returns True if there is any object that
appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates.
Solution: http://thinkpython2.com/code/has_duplicates.py
"""

def has_duplicates(li):
    dictionary = dict()   
    for word in li:
        if word in dictionary:
            return True
        dictionary[word] = True
    return False
