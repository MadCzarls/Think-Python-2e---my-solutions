#!/usr/bin/env python3

"""
Exercise 3.3.
Note:  This exercise should be done using only the statements and other features we
have learned so far.

1.  Write a function that draws a grid like the following:

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +

    Hint: to print more than one value on a line, you can print a comma-separated
    sequence of values:

    print('+', '-')

    By default, print advances to the next line, but you can override that behavior
    and put a space at the end, like this:

    print('+', end=' ')
    print('-')

    The output of these statements is '+ -'.
    A print statement with no argument ends the current line and goes to the next line.

2.  Write a function that draws a similar grid with four rows and four columns.

Solution: http://thinkpython2.com/code/grid.py
Credit: This exercise is based on an exercise in 
Oualline, Practical C Programming, Third Edition, O’Reilly Media, 1997.
"""

# first way:
def print_four_times(bruce):
    print(bruce)
    print(bruce)
    print(bruce)
    print(bruce)

def print_grid_1a():
    border = ('+ ' + '- ' * 4) * 2 + '+'
    middle = '|         |         |'
    print(border)
    print_four_times(middle)
    print(border)
    print_four_times(middle)
    print(border)


# second way:
def print_grid_1b():
    border = '+ - - - - + - - - - +'
    middle = '|         |         |'
    print(border)
    print_four_times(middle)
    print(border)
    print_four_times(middle)
    print(border)

    
print_grid_1a()
print_grid_1b()

print('*-' * 30) # to separate printed results of functions from different tasks 
# second task:

def print_grid_2():
    border = ('+ ' + '- ' * 4) * 4 + '+'
    middle = ('|' + ' ' * 9) * 4 + '|'
    print(border)
    print_four_times(middle)
    print(border)
    print_four_times(middle)
    print(border)
    print_four_times(middle)
    print(border)
    print_four_times(middle)
    print(border)
    
print_grid_2()
