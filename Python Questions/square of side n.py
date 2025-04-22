"""
Square of side 'N'
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

Input Parameters:

n (int): The size of the square (number of rows and columns).

Output:

A list of strings where each string is a row of n characters.



Example:

Input: 3
Output: ['***', '***', '***']
 
Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']
"""

def generate_square(n):
    square= []
    for i in range(n):
        element = n*'*'
        square.append(element)

    return square

print(generate_square(5))