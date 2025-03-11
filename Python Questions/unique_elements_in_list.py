"""
Check if All Elements in a List are Unique

You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.

Parameters:

lst (List of integers): The list of integers to check for uniqueness.

Returns:

A boolean value True if all elements in the list are unique, False otherwise.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: True

Input: lst = [1, 2, 3, 3, 4, 5]
Output: False
"""

def check_unique(lst):
    new_list = []
    for element in lst:
        if element not in new_list:
            new_list.append(element)
        else:
            return False

    return True