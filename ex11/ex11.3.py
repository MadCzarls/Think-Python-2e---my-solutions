#!/usr/bin/env python3

"""
Exercise 11.3.
Memoize the Ackermann function from Exercise 6.2 and see if memoization makes it
possible to evaluate the function with bigger arguments. Hint:no.

def ack(m, n):
    '''Ackermann's function;
    m, n - integers greater-than-equal 0
    '''
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

print(ack(3, 4))

Solution: http://thinkpython2.com/code/ackermann_memo.py
"""

# Could't figure it out; the idea (and usefullness) of memoization doesn't seem
# clear to me. 
# Author himself in his solution uses try statement which was not covered in the
# book till now which sort of confuses even more^^
