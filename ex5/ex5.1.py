#!/usr/bin/env python3

"""
Exercise 5.1.
The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a
reference point. On UNIX systems, the epoch is 1 January 1970.

>>> import time
>>> time.time()
1437746094.5735958

Write a script that reads the current time and converts it to a time of day
in hours, minutes, and seconds, plus the number of days since the epoch.
"""

import time
last_epoch = time.time()

def current_time(since_epoch):
    """Calculates current hour, minute, and second since given epoch;
    since epoch - in seconds.
    """
    hours_since = since_epoch // 60 // 60
    current_hour = hours_since - (hours_since // 24) * 24
    minutes_since = since_epoch // 60
    current_minute = minutes_since - (minutes_since // 60) * 60
    second_since = since_epoch // 1  # to round down seconds
    current_second = second_since - (second_since // 60) * 60
    return current_hour, current_minute, current_second

def days_since_epoch(epoch):
    """Returns number of days since given epoch;
    epoch - in seconds.
    """
    days = epoch // 60 // 60 // 24
    return days


print(current_time(last_epoch))
print(days_since_epoch(last_epoch))
