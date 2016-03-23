#!/usr/bin/env python3

"""
Exercise 4.2.
Write an appropriately general set of functions that can draw flowers as in
Figure 4.1.

Solution: http://thinkpython2.com/code/pie.py
"""

import turtle
import math

bob = turtle.Turtle()

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()

def isosceles(t, side_length, angle_between_sides):
    """Draws isosceles triangle with given side.
    t = Turtle
    n = number of triangles in pie
    """
    angle_by_basis = 180 - 90 - (angle_between_sides / 2)
    base_length = 2 *(side_length * math.cos(angle_by_basis * math.pi / 180))

    t.fd(side_length)
    t.lt(180 - angle_by_basis)
    t.fd(base_length)
    t.lt(180 - angle_by_basis)
    t.fd(side_length)
    
def pie(t, n, side_length):
    """Draws a pie with given (n) number of triangles.
    t = Turtle
    """
    
    angle = 360 / n
    angle_by_basis = 180 - 90 - (angle / 2)
    
    for i in range(n):
        isosceles(bob, side_length, angle)
        t.lt(180)
        
move(bob, -100)
pie(bob, 5, 40)

move(bob, 100)
pie(bob, 6, 40)

move(bob, 100)
pie(bob, 7, 40)

turtle.mainloop()
