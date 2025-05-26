#!/usr/bin/env python3
# Author: Andrea Arriola Gamboa
# Course: Computational Methods for Bioinformatics
# Python version: 3.12.9

"""
String manipulation practice for Computational Methods for Bioinformatics.

This script contains several standalone functions to practice string operations
in preparation for the Computational Methods for Bioinformatics exam.

To run a specific function, uncomment the corresponding function call
below the function of interest.

Note: This script was intended for interactive learning and experimentation.
"""

def ReverseString(st):
    """This function returns the given string but reversed."""
    reverse = st[::-1]
    return reverse

#st = input("Please type a string and I will reverse it: ")
#print(ReverseString(st))

def PalindromeCheck(word):
    """This function checks if a word given by the user is a palindrome."""
    caps = word.upper()
    final = caps.replace(" ","")
    return final == final[::-1]

#word = input("Please type a word and I'll check if it's a palindrome: ")
#print(PalindromeCheck(word))

def CountVowels(word):
    """This function counts and outputs how many vowels a word given by a user has."""
    upperword = word.upper()
    vowels = []
    
    for letra in upperword:
        if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
            vowels.append(letra)
    
    return "The word has "+str(len(vowels))+" vowels."

#word = input("Please input a word. I will count how many vowels it has: ")
#print(CountVowels(word))

def ReplaceSpaces(string):
    """This function takes a string from the user and replaces the spaces for a hyphen."""
    newstring = string.replace(" ","-")
    return newstring

#string = input("Please write a sentence: ")
#print(ReplaceSpaces(string))

def FindSubstring(string,substring):
    '''This function finds a substring inside a given string'''
    CapsString = string.upper()
    CapsSubstring = substring.upper()
    finder = CapsString.find(CapsSubstring)
    return finder

#string = input("Insert a string: ")
#substring = input("Insert the substring that you want to find: ")
#print(FindSubstring(string,substring))

def RemoveDuplicates(word):
    '''This function removes duplicated letters from a given string'''
    result = ""
    for character in word:
        if character not in result:
            result = result + character
    return result

#word = input("Insert a string, I will remove the duplicated characters: ")
#print(RemoveDuplicates(word))

def SwapCase(string):
    '''This function swaps the case of each letter in a given string (From uppercase to lowercase and viceversa).'''
    result = string.swapcase()
    return result

#string = input("Give me a string to swap the cases: ")
#print(SwapCase(string))

def LongestWord(sentence):
    '''This function returns the longest word in a given string.'''
    SplatSentence = sentence.split()
    LongestLen = 0
    LongestWord = ""
    
    for words in SplatSentence:
        if len(words) > LongestLen:
            LongestWord = words
    return LongestWord

#sentence = input("Insert a sentence, I will find the longest word: ")
#print(LongestWord(sentence))

def AnagramChecker(word1,word2):
    '''This function takes two strings given by the user and checks if they're anagrams.'''
    FirstWord = word1.upper().replace(" ","")
    SecondWord = word2.upper().replace(" ","")
    
    return sorted(FirstWord) == sorted(SecondWord)

#word1 = input("Insert word 1: ")
#word2 = input("Insert word 2: ")
#print(AnagramChecker(word1,word2))