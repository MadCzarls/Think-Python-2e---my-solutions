#!/usr/bin/env python3

"""
Exercise 10.11.
Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list.

Solution: http://thinkpython2.com/code/
"""

import bisect

def word_list(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)
    return li


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


def reverse_pair(li):
    list_of_pairs = []
    for word in li:
        if in_bisect_cheat(li, word[::-1]):
            pair = (word, word[::-1])
            list_of_pairs.append(pair)
    return list_of_pairs


li = word_list("words.txt")
print(reverse_pair(li))

