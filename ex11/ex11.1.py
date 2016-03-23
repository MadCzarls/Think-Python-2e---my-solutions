#!/usr/bin/env python3

"""
Exercise 11.1.
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the
in operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 10.10, you can compare the speed of this implementation with the list
in operator and the bisection search.
"""

def make_dict(file_input):
    dictionary = dict()
    word_list = []
    
    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)
    
    index = 0
    for word in word_list:
        dictionary[word] = index
        index += 1
    return dictionary


def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False


dictionary = make_dict("words.txt")
print(word_hunter('bike', dictionary))
print(word_hunter('leleleleelel', dictionary))
