#!/usr/bin/env python3

"""
Exercise 10.12.
Two words “interlock” if taking alternating letters from each forms a new word.
For example, “shoe” and “cold” interlock to form “schooled”.

Solution: http://thinkpython2.com/code/interlock.py

Credit: This exercise is inspired by an example at http://puzzlers.org

1.  Write a program that finds all pairs of words that interlock.
    Hint: don’t enumerate all pairs!

2.  Can you find any words that are three-way interlocked; that is, every third
    letter forms a word, starting from the first, second or third?
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


def interlock(word_list):
    interlocking_words = []
    for word in word_list:
        if in_bisect_cheat(word_list, word[::2]) and in_bisect_cheat(word_list, word[1::2]):
             interlockers = (word[::2], word[1::2], word)
             interlocking_words.append(interlockers)
    return interlocking_words


def three_way_interlock(word_list):
    interlocking_words = []
    for word in word_list:
        if in_bisect_cheat(word_list, word[::3]) and in_bisect_cheat(word_list, word[1::3]) \
        and in_bisect_cheat(word_list, word[2::3]):
             interlockers = (word[::3], word[1::3], word[2::3], word)
             interlocking_words.append(interlockers)
    return interlocking_words


# Answer1:
li = word_list("words.txt")
print(interlock(li))
print()

# Answer2:
print(three_way_interlock(li))
