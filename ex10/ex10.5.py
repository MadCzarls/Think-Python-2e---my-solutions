#!/usr/bin/env python3

"""
Exercise 10.5.
Write a function called is_sorted that takes a list as a parameter and returns
True if the list is sorted in ascending order and False otherwise. For example:

>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b','a'])
False
"""

def is_sorted(li):
    return li == sorted(li)


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
print(is_sorted(['a', 'a']))
print(is_sorted(['a', 'b']))
print(is_sorted([2, 1]))
print(is_sorted([1, 2, 3, 4, 3]))
