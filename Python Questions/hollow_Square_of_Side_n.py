"""
Hollow Square of side 'N'
Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:

n (int): The size of the square (number of rows and columns).

Output:

A list of strings where each string is a row of n characters, representing a hollow square.

Example:

Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']

"""

def generate_hollow_square(n):
    square = []
    for i in range(n):
        if i ==0 or i ==n-1:
            element = n*'*'
            square.append(element)

        else:
            element = '*' + (n-2)*' ' + '*'
            square.append(element)
    return square


print(generate_hollow_square(0))