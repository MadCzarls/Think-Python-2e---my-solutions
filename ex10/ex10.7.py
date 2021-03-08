#!/usr/bin/env python3

"""
Exercise 10.7.
Write a function called has_duplicates that takes a list and returns True
if there is any element that appears more than once. It should not modify the
original list.
"""

def has_duplicates(elements):
    new_list = list(elements)
    for i in new_list:
        if new_list.count(i) > 1:
            return True
    return False






t = [4, 7, 2, 7, 3, 8, 9 ]
print(has_duplicates(t))
print(has_duplicates(['b', 'd', 'a', 't']))

print(has_duplicates(['']))
print(has_duplicates([5, 7, 9, 2, 4, 1, 8,]))
