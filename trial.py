# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 00:13:46 2018

@author: CyberCloned

"""


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

for word in wordlist:
    
    if word[1] == "t" and word[len(word)-1] == "t":
    
        print(word)