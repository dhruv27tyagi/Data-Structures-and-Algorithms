"""
Given a list of integers, write a function to find the sum of all the elements in the list.



Input Parameters:

lst (List[int]): A list of integers.

Output:

int: The sum of all the elements in the list.



Example:

Input: lst = [7]
Output: 7
 
Input: lst = [-1, -2, -3, -4]
Output: -10
 
Input: lst = [1, 2, 3, 4, 5]
Output: 15
"""

def sum_of_elements(lst):

    sum = 0
    for number in lst:
        sum = sum + number

    return sum