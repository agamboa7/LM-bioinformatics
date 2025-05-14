#!/usr/bin/env python3
# Author: Andrea Arriola Gamboa
# Course: Computational Methods for Bioinformatics
# Python version: 3.12.9

"""
This program reads a user-input string and extracts only the characters
that represent DNA bases: A, C, G, and T. It then prints the valid DNA sequence
and its complementary sequence based on standard base pairing rules.

This exercise was created as part of the course "Computational Methods for Bioinformatics"
taught by Professor Ivan Lanese at the University of Bologna, during the first semester
of the master's program.

The purpose of the exercise was to practice basic programming concepts such as:
- Strings
- Lists
- If statements
"""

# I. Write a program that prints only characters ACGT in a given string

# Get input from the user
input_string = input("Write a string: ")
# Convert the input to uppercase to handle lowercase letters
input_string_upper = input_string.upper()
# List to store valid nucleotide bases
ACGT_list = []

# Filter only A, C, G, T characters
for letter in input_string_upper:
    if letter == "A":
        ACGT_list.append(letter)
    elif letter == "T":
        ACGT_list.append(letter)
    elif letter == "G":
        ACGT_list.append(letter)
    elif letter == "C":
        ACGT_list.append(letter)

# Join the valid bases into a string
final_string = "".join(ACGT_list)
print("Sequence:  ", final_string)

# II. With the previous string, generate the complementary sequence
complementary_bases = []

for base in final_string:
    if base == "A":
        complementary_bases.append("T")
    elif base == "T":
        complementary_bases.append("A")
    elif base == "G":
        complementary_bases.append("C")
    elif base == "C":
        complementary_bases.append("G")

complementary_string = "".join(complementary_bases)
print("Complement:", complementary_string)