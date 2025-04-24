"""
Merge two Sorted List
Merge Two Sorted Lists

You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. The resulting list should also be in non-decreasing order.

Parameters:

list1 (List of integers): The first sorted list.

list2 (List of integers): The second sorted list.

Returns:

A single list of integers, containing all elements from list1 and list2, sorted in non-decreasing order.

Example:

Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: list1 = [1, 4, 7], list2 = [2, 3, 5, 8]
Output: [1, 2, 3, 4, 5, 7, 8]
"""

def merge_lists(list1,list2):
    i, j = 0, 0
    result = []  # Initialize an empty list to store the merged result
 
    # Traverse both lists and merge them in sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])  # Add the smaller element to the result list
            i += 1
        else:
            result.append(list2[j])  # Add the smaller element to the result list
            j += 1
 
    # If there are remaining elements in list1, add them to the result
    while i < len(list1):
        result.append(list1[i])
        i += 1
 
    # If there are remaining elements in list2, add them to the result
    while j < len(list2):
        result.append(list2[j])
        j += 1
 
    return result
print(merge_lists([2,3,7],[1,4,5,6]))