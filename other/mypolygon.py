#!/usr/bin/env python3

import turtle
import math
bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    # 360-sided polygon, number of sides equals to umber of
    # degrees in full circle, to have perfect circle
    n = 360 
    
    circumference = 2 * math.pi * r
    lenght = circumference / n
    polygon(t, lenght, n)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    arc_lenght = circumference * angle / 360
    step_lenght = arc_lenght / 360
    step_angle = angle / 360
    
    for i in range(n):
        t.fd(step_lenght)
        t.lt(step_angle)
    
arc(bob,50, 90)

turtle.mainloop()


