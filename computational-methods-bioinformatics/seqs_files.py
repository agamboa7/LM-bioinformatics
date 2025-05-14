#!/usr/bin/env python3
# Author: Andrea Arriola Gamboa
# Course: Computational Methods for Bioinformatics
# Python version: 3.12.9

"""
This program processes a file ('sequences.seq.txt') containing DNA sequences
and answers the following five questions:

A) How many sequences are in the file?
B) How many sequences contain the pattern 'CTATA'?
C) How many sequences have more than 1000 bases?
D) How many sequences have a GC composition greater than 50%?
E) How many sequences have both: more than 2000 bases and >50% GC content?

This exercise was created as part of the course "Computational Methods for Bioinformatics"
taught by Professor Ivan Lanese at the University of Bologna, during the first semester
of the master's program, and it was designed to practice working with:
- File input and iteration
- String operations
- Lists
- Conditional logic

Required files:
Make sure that the file 'sequences.seq.txt' is in the same directory as this script.
This text file was provided by Professor Ivan Lanese as part of the coursework materials.
"""

# A) How many sequences are in the file?
total_A = 0
seqs = open("sequences.seq.txt", "r")
for line in seqs:
    total_A = total_A + 1
print("Number of sequences:", total_A)
seqs.close()

# B) How many contain the pattern 'CTATA'?
list_B = []
seqs = open("sequences.seq.txt", "r")
for ctata in seqs:
    if "CTATA" in ctata:
        list_B.append(ctata)
print("Number of sequences that contain 'CTATA':", len(list_B))
seqs.close()

# C) How many have more than 1000 bases?
list_C = []
seqs = open("sequences.seq.txt", "r")
for line in seqs:
    if len(line.strip()) > 1000:
        list_C.append(line)
print("Number of sequences with more than 1000 bases:", len(list_C))
seqs.close()

# D) How many have over 50% GC composition?
list_D = []
seqs = open("sequences.seq.txt", "r")
for fifty_gc in seqs:
    seq = fifty_gc.strip()
    G = seq.count("G")
    C = seq.count("C")
    gc_total = G + C
    if gc_total > len(seq) / 2:
        list_D.append(seq)
print("Number of sequences with over 50% GC:", len(list_D))
seqs.close()

# E) How many have more than 2000 bases and more than 50% GC composition?
list_E = []
seqs = open("sequences.seq.txt", "r")
for line in seqs:
    seq = line.strip()
    G = seq.count("G")
    C = seq.count("C")
    gc_total = G + C
    if len(seq) > 2000 and gc_total > len(seq) / 2:
        list_E.append(seq)
print("Number of sequences with >2000 bases and >50% GC:", len(list_E))
seqs.close()
