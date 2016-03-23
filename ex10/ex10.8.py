#!/usr/bin/env python3

"""
Exercise 10.8.
This exercise pertains to the so-called Birthday Paradox, which you can read about
at http://en.wikipedia.org/wiki/Birthday_paradox .

If there are 23 students in your class, what are the chances that two of you have
the same birthday? You can estimate this probability by generating random samples
of 23 birthdays and checking for matches.
Hint: you can generate random birthdays with the randint function in the random
module.

You can download my solution from
http://thinkpython2.com/code/birthday.py
"""

from random import randint

def date_generator(pupils):
    dates = []
    for student in range(pupils):
        dates.append(randint(1, 366))
    return dates


def has_matches(dates):
    dates.sort()
    for i in range(len(dates) -1):
        if dates[i] == dates[i + 1]:
            return True
    return False


def chances(num_of_simulations, pupils):
    matches = 0
    
    for i in range(num_of_simulations):
        dates = date_generator(pupils)
        if has_matches(dates):
            matches += 1
    
    print("There are {} classes having students with the same birthday date".format(matches))
    print("in {} simulations.".format(num_of_simulations))


chances(1000, 23)
