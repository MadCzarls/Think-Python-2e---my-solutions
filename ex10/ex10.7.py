#!/usr/bin/env python3

"""
Exercise 10.7.
Write a function called has_duplicates that takes a list and returns True
if there is any element that appears more than once. It should not modify the
original list.
"""

def has_duplicates(li):
    if len(li) == 0:
        return "List is empty."
    elif len(li) == 1:
        return "List contains only one element."
    
    previous_elem = li[0]
    for elem in sorted(li):
        if previous_elem == elem:
            return True
        previous_elem = elem
    return False


t = [4, 7, 2, 7, 3, 8, 9 ]
print(has_duplicates(t))
print(has_duplicates(['b', 'd', 'a', 't']))
print(has_duplicates([]))
print(has_duplicates(['']))
print(has_duplicates([5, 7, 9, 2, 4, 1, 8,]))
