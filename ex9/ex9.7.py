#!/usr/bin/env python3

"""
Exercise 9.7.
This question is based on a Puzzler that was broadcast on the radio program
Car Talk (http://www.cartalk.com/content/puzzlers):

Give me a word with three consecutive double letters. I’ll give you a couple of
words that almost qualify, but don’t. For example, the word committee,
c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there.
Or Mississippi: M-i-s-s-i-s-s-i-p-p-i.
If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only
word. Of course there are probably 500 more but I can only think of one.
What is the word?

Write a program to find it.
Solution: http://thinkpython2.com/code/cartalk1.py
"""

def searched_word(word):
    count = 0
    index = 0
    while index < len(word) - 1:
        if word[index] == word[index + 1]:
            count += 1
            if count == 3:
                return True
            index += 2
        else:
            count = 0
            index += 1


fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if searched_word(word) == True:
        print(word)
        count += 1
print(count)

# There are 4 words with three consecutive double letters in words.txt.
