#!/usr/bin/env python3

"""
The following exercise use the turtle module, described in Chapter 4.

Exercise 5.6.
The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
curve with length x, all you have to do is:

1.  Draw a Koch curve with length x/3.
2.  Turn left 60 degrees.
3.  Draw a Koch curve with length x/3.
4.  Turn right 120 degrees.
5.  Draw a Koch curve with length x/3.
6.  Turn left 60 degrees.
7.  Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight
line with length x.

1.  Write a function called koch that takes a turtle and a length as parameters,
    and that uses the turtle to draw a Koch curve with the given length.

2.  Write a function called snowflake that draws three Koch curves to make the
    outline of a snowflake.
    Solution: http://thinkpython2.com/code/koch.py .

3.  The Koch curve can be generalized in several ways. See
    http://en.wikipedia.org/wiki/Koch_snowflake
    for examples and implement your favorite.
"""

import turtle
bob = turtle.Turtle()

def koch(turtle, length):
    if length < 3:
        turtle.fd(length)
        return
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)
    turtle.rt(120)
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)

def snowflake(turtle, length):
    for i in range(3):
        koch(turtle, length)
        turtle.rt(120)

koch(bob, 30)

bob.pu()
bob.fd(50)
bob.pd()

snowflake(bob, 30)

turtle.mainloop()
