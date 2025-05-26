#!/usr/bin/env python3
# Author: Andrea Arriola Gamboa
# Course: Computational Methods for Bioinformatics
# Python version: 3.12.9

"""
List manipulation practice for Computational Methods for Bioinformatics.

This script contains several standalone functions to practice list operations
and for loops in preparation for the Computational Methods for Bioinformatics exam.

To run a specific function, uncomment the corresponding function call
below the function of interest.

Note: This script was intended for interactive learning and experimentation.
"""

def SumList():
    '''This function sums all numbers in a list given by the user.'''
    inp = input("Insert the numbers you want to sum, separated by a space: ")
    lista = list(map(int, inp.split()))
    total = 0
    for num in lista:
        total = total + num
    return total

#print(SumList())

def LargestSmallest():
    '''This function finds the largest and smallest values in a list given by the user.'''
    user_input = input("Insert the numbers you want to add in the list, separated by a space: ")
    numbers_list = list(map(int,user_input.split()))
    _max = 0
    for num in numbers_list:
        if num > _max:
            _max = num
    _min = _max
    for ber in numbers_list:
        if ber < _min:
            _min = ber
    return _max, _min

#print(LargestSmallest())

def RemoveDuplicates():
    '''This function removes duplicates from a list given by the user.'''
    user_list = input("Insert a list of numbers separated by a space: ")
    number_list = list(map(int,user_list.split()))
    new_list = []
    for num in number_list:
        if num not in new_list:
            new_list.append(num)
    return new_list

#print(RemoveDuplicates())
    
def CountElements():
    '''This functions counts how many times an element is on a list.
    The list is set by the program but the input is the element to count.'''
    _list = [1,1,2,3,4,5,5,6,7,7,7,8,9,9,9]
    user_input = int(input("Type a number from 1 to 10 and I will count how many times it is on the list: "))
    c = 0
    for num in _list:
        if num == user_input:
            c = c+1
    return c

#print(CountElements())

def SecondMax():
    '''This function finds the second max number in a list given by the user. '''
    user_list = input("Give me a list of numbers, separated by a space: ")
    numbers_list = list(map(int,user_list.split()))
    max_num = 0
    for num in numbers_list:
        if num > max_num:
            max_num = num
    second_max_num = 0
    for sec in numbers_list:
        if sec > second_max_num and sec < max_num:
            second_max_num = sec
    return second_max_num

#print(SecondMax())

def ReverseList():
    '''This function reverses a list given by the user.'''
    user_list = input("Insert a list of numbers separated by a space: ")
    numbers_list = list(map(int,user_list.split()))
    return numbers_list[::-1]

#print(ReverseList())

def CheckSort():
    '''This function checks if a list given by the user is sorted and returns True or False.'''
    user_list = input("Insert the numbers of the list, separated by a space: ")
    numbers_list = list(map(int,user_list.split()))
    sorted_list = sorted(numbers_list)
    return numbers_list == sorted_list

#print(CheckSort())

def RotateList():
    '''This function rotates a list to the right by n places.'''
    user_list = input("Write a list of numbers separated by spaces: ")
    n = int(input("Write how many places you would like to rotate it (n): "))
    number_list = list(map(int,user_list.split()))
    new_list = []
    i = -1
    for num in number_list:
        i = i+1
        if num >= number_list[-n]:
            new_list.append(num)
    for nums in number_list:
        if nums < number_list[-n]:
            new_list.append(nums)
    return new_list

#print(RotateList())

def ListIntersection():
    '''This functions finds the common elements in two lists given by the user.'''
    list1 = input("Insert the first list of numbers (separated by a space): ")
    list2 = input("Insert the second list of numbers (separated by a space): ")
    numbers1 = list(map(int,list1.split()))
    numbers2 = list(map(int,list2.split()))
    intersection = []
    
    for num in numbers1:
        if num in numbers2:
            intersection.append(num)
    return intersection

#print(ListIntersection())