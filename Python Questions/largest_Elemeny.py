"""
Largest Element in a List
Find the Largest Element in a List

Write a Python function that finds and returns the largest element in a given list of integers.

Parameters:

numbers (List of integers): The input list containing integers.

Returns:

An integer representing the largest element in the input list.

Example:

Input: numbers = [3, 8, 2, 10, 5]
Output: 10

Input: numbers = [-5, -10, -2, -1, -7]
Output: -1
"""

def largest(arr):
    largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest 

print(largest([3,6,5,1,8]))