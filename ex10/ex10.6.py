#!/usr/bin/env python3

"""
Exercise 10.6.
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True
if they are anagrams.
"""

def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)

print(is_anagram('abba', 'baba'))
print(is_anagram('lol', 'kol'))
print(is_anagram('a', 'b'))
print(is_anagram('', 'a'))
