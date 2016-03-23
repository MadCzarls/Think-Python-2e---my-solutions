#!/usr/bin/env python3

"""
Exercise 10.2.
Write a function called cumsum that takes a list of numbers and returns the
cumulative sum; that is, a new list where the ith element is the sum of the first
i + 1 elements from the original list. For example:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""

def cumsum(li):
    result = []
    total = 0
    for elem in li:
        total += elem
        result.append(total)
    return result


t = [1, 2, 3]
print(cumsum(t))
