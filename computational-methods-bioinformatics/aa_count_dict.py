#!/usr/bin/env python3
# Author: Andrea Arriola Gamboa
# Course: Computational Methods for Bioinformatics
# Python version: 3.12.9

"""
Amino Acid Counting Script

This script was created to practice using Python dictionaries,
focusing on counting elements in a protein sequence using
standard one-letter amino acid codes.

This exercise was created during the course "Computational Methods
for Bioinformatics" taught by Professor Ivan Lanese at the University
of Bologna, during the first semester of the master's program

"""

# Count each amino acid in a protein sequence

# Example protein sequence
protein_seq = (
    "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGL"
    "AHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
)

# Standard 20 amino acid one-letter codes
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Initialize dictionary to store counts
aa_counts = {}

# Count occurrences of each amino acid
for aa in amino_acids:
    aa_counts[aa] = protein_seq.count(aa)

# Print the results
print("Amino acid counts in the sequence:")
for aa in aa_counts:
    print(aa,"=",aa_counts[aa])
