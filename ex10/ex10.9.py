#!/usr/bin/env python3

"""
Exercise 10.9.
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method
and the other using the idiom t = t + [x]. Which one takes longer to run? Why?
"""

def version1(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)
    
    return li


def version2(file):
    fin = open(file)
    t = []
    
    for line in fin:
        x = line.strip()
        t = t + [x]


# version1("words.txt")
# version2("words.txt")
# Second version of the function takes much longer.
# I suppose it's because it needs to initialize the list 't' each time when 
# new word is being added to it and create a new list with each new word - [x].
# Consequently with each word it takes longer because each singleton needs to be
# stored in memory until the function stops running.
