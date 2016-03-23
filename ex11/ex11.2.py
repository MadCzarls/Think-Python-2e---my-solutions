#!/usr/bin/env python3

"""
Exercise 11.2.
Read the documentation of the dictionary method setdefault and use it to write a
more concise version of invert_dict.

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

Solution: http://thinkpython2.com/code/invert_dict.py
"""

def invert_dict(d):
    inverse = dict()
    for key in d:
        value = d[key]
        inverse.setdefault(value, []).append(key)
    return inverse
        
