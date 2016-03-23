#!/usr/bin/env python3

"""
Exercise 11.6.
Here’s another Puzzler from Car Talk (http://www.cartalk.com/content/puzzlers):

This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable,
five-letter word recently that has the following unique property. When you remove
the first letter, the remaining letters form a homophone of the original word,
that is a word that sounds exactly the same. Replace the first letter, that is,
put it back and remove the second letter and the result is yet another homophone
of the original word. And the question is, what’s the word?

Now I’m going to give you an example that doesn’t work.  Let’s look at the
five-letter word, ‘wrack.’  W-R-A-C-K, you know like to ‘wrack with pain.’
If I remove the first letter, I am left with a four-letter word, ’R-A-C-K.’ As in,
‘Holy cow, did you see the rack on that buck! It must have been a nine-pointer!’
It’s a perfect homophone. If you put the ‘w’ back, and remove the ‘r,’ instead,
you’re left with the word, ‘wack,’ which is a real word, it’s just not a homophone
of the other two words.
But there is, however, at least one word that Dan and we know of, which will yield
two homophones if you remove either of the first two letters to make two, new
four-letter words. The question is, what’s the word?

You can use the dictionary from Exercise 11.1 to check whether a string is in
the word list.

To check whether two words are homophones, you can use the CMU Pronouncing Dictionary.
You can download it from http://www.speech.cs.cmu.edu/cgi- bin/cmudict
or from http://thinkpython2.com/code/c06d 
and you can also download http://thinkpython2.com/code/pronounce.py
which provides a function named read_dictionary that reads the pronouncing
dictionary and returns a Python dictionary that maps from each word to a string
that describes its primary pronunciation.

Write a program that lists all the words that solve the Puzzler.
Solution: http://thinkpython2.com/code/homophone.py
"""

def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


def word_hunter(word, dictionary):
    if word in dictionary:
        return True
    return False


def homophones(word_dict):
    li = []
    for word in word_dict:
        homophone1 = word[1::]
        homophone2 = word[0] + word[2:]
        
        if word_hunter(homophone1, word_dict) and word_hunter(homophone2, word_dict):
            if word_dict[word] == word_dict[homophone1] and word_dict[word] == word_dict[homophone2]:
                li.append(word)
    return li


dictionary = read_dictionary()
t = homophones(dictionary)  # all word in CMU Pronouncing Dictionary which fullfill the conditions


# finding words with length=5 ("He came upon a (...)five-letter word")
# that are in homophones list and in words.txt

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

word_list = make_dict("words.txt")


for word in t:
    if len(word) == 5 and word_hunter(word, word_list):
        print(word)
