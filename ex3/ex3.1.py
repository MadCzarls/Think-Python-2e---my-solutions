#!/usr/bin/env python3

"""
Exercise 3.1.
Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the
string is in column 70 of the display.

>>> right_justify('monty')
                                                                     monty

Hint: Use string concatenation and repetition. Also, Python provides a built-in
function called len that returns the length of a string, so the value of len('monty')
is 5.
"""

def right_justify(s):
    num_of_spaces = 70 - len(s)
    result = num_of_spaces * " " + s
    print(result)

right_justify("monty") 
