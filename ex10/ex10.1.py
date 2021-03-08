#!/usr/bin/env python3

"""
Exercise 10.1.
Write a function called nested_sum that takes a list of lists of integers and
adds up the elements from all of the nested lists. For example:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""

def nested_sum(list_int):
  total = 0
  for i in list_int:
    for j in i:
      total += j
  return total


t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)
