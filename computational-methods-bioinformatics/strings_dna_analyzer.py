#!/usr/bin/env python3
# Author: Andrea Arriola Gamboa
# Course: Computational Methods for Bioinformatics
# Python version: 3.12.9

"""
Simple DNA sequence analyzer.

This script prompts the user to input a DNA sequence and:
- Converts the sequence to uppercase.
- Calculates the length of the sequence.
- Counts the number of each nucleotide (A, T, C, G).

The purpose of the exercise was to comprehend and practice basic strings functions.

"""

# Get user input
dna_sequence = input("Please type a DNA sequence to analyse it: ")

# Convert to uppercase for consistent analysis
dna_upper = dna_sequence.upper()
print("Sequence is:", dna_upper)

# Calculate length
sequence_length = len(dna_upper)
print("It is", sequence_length, "bases long")

# Count nucleotides
count_A = dna_upper.count("A")
count_T = dna_upper.count("T")
count_C = dna_upper.count("C")
count_G = dna_upper.count("G")

# Print results
print("Adenine (A):", count_A)
print("Thymine (T):", count_T)
print("Cytosine (C):", count_C)
print("Guanine (G):", count_G)