#!/usr/bin/env python3

"""
Exercise 9.6.
Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words
are there?
"""

def is_abecedarian(word):
    previous_letter = word[0]
    for letter in word:
        if ord(letter) < ord(previous_letter):
            return False
        previous_letter = letter
    return True


fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if is_abecedarian(word) == True:
        print(word)
        count += 1
print(count)

# How many abecedarian words are there?
# 596
