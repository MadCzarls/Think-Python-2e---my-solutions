#!/usr/bin/env python3

"""
Exercise 5.3.
If you are given three sticks, you may or may not be able to arrange them in
a triangle. For example, if one of the sticks is 12 inches long and the other
two are one inch long, you will not be able to get the short sticks to meet in
the middle.  For any three lengths, there is a simple test to see if it is
possible to form a triangle:

    If any of the three lengths is greater than the sum of the other two, then
you cannot form a triangle.  Otherwise, you can.  (If the sum of two lengths
equals the third, they form what is called a “degenerate” triangle.)

1.  Write a function named is_triangle that takes three integers as arguments,
    and that prints either “Yes” or “No”, depending on whether you can or cannot
    form a triangle from sticks with the given lengths.

2.  Write a function that prompts the user to input three stick lengths,
    converts them to integers, and uses is_triangle to check whether sticks
    with the given lengths can form a triangle.
"""


def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    elif (a == b + c) or (b == a + c) or (c == a + b):
        print("Degenerate")
    else:
        print("Yes")


def prompting():
    a = int(float(input("Type length of side a: ")))
    b = int(float(input("Type length of side b: ")))
    c = int(float(input("Type length of side c: ")))

    is_triangle(a, b, c)


prompting()
