#!/usr/bin/env python3

"""
Exercise 7.1.
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.

To test it, write a function named test_square_root that prints a table like this:

a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0

The first column is a number, a;
the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between the two estimates.
"""

# my table in not formatted identical with given one; no idea how to do it like this;

import math

def mysqrt(a):
    """Calculates square root using Newton's method:
    https://en.wikipedia.org/wiki/Newton's_method
    
    a - positive integer < 0;
    x - estimated value, in this case a/2
    """
    x = a/2
    while True:
        estimated_root = (x + a/x) / 2
        if estimated_root == x:
            return estimated_root
            break
        x = estimated_root

def test_square_root():
    """Displays outcomes of calculating square root of a using different methods;
    list_of_a - list of positive digit.
    """
    print("a   mysqrt(a)     math.sqrt(a)  diff")
    print("-   ---------     ------------  ----")
    
    for i in range (1, 10):
        
        check_list = {i: [mysqrt(i), math.sqrt(i)]}

        for k, v in check_list.items():
            diff = math.sqrt(i) - mysqrt(i)
            print("{:<3} {:<13.11} {:<13.11} {:<10.11}".format(i, mysqrt(i), math.sqrt(i), diff)


test_square_root()
