#!/usr/bin/env python3

"""
Exercise 4.1
Download the code in this chapter from http://thinkpython2.com/code/polygon.py


1.  Draw a stack diagram that shows the state of the program while executing
    circle(bob, radius). You can do the arithmetic by hand or add print statement
    to the code.
     
2.  The version of arc in Section 4.7 is not very accurate because the linear
    approximation of the circle is always outside the true circle. As a result,
    the Turtle ends up a few pixels away from the correct destination. My solution
    shows a way to reduce the effect of this error. Read the code and see if it
    makes sense to you. If you draw a diagram, you might see how it works.
"""

import turtle
import math

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


bob = turtle.Turtle()
radius = 100

# moves the starting point of turtle, quite redundant
bob.pu()
bob.fd(radius)
bob.lt(90)
bob.pd()

circle(bob,radius)
# wait for the user to close the window
turtle.mainloop()

# stack diagram

'''

__main__ :
    bob    ---> turtle.Turtle()
    radius ---> 100

polyline:
    t      ---> bob
    n      ---> 158
    length ---> 3.9766995615060674
    angle  ---> 2.278481012658228

arc :
    t           ---> bob
    r           ---> 100
    angle       ---> 360
    arc_length  ---> 628.3185307179587
    n           ---> 158
    step_length ---> 3.9766995615060674
    step_angle  ---> 2.278481012658228
    
circle :
      t ---> bob
      r ---> 100
      
'''

