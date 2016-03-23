#!/usr/bin/env python3

"""
Exercise 6.2.
The Ackermann function, A(m, n), is defined:

    https://en.wikipedia.org/wiki/Ackermann_function

Write a function named ack that evaluates the Ackermann function. Use your
function to evaluate ack(3, 4), which should be 125. What happens for larger
values of m and n?

Solution: http://thinkpython2.com/code/ackermann.py
"""

def ack(m, n):
    """Ackermann's function;
    m, n - integers greater-than-equal 0
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

print(ack(3, 4))
