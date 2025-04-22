"""
Pyramid Pattern
Problem Description:

You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.

Input:

A single integer n, where 1 <= n <= 100.

Output:

A list of strings where each string contains stars ('*') centered, forming a pyramid shape. Each row has an increasing number of stars, with appropriate spaces for centering.

Example:

Input: 3
Output: ['  *  ', ' *** ', '*****']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']

"""

def generate_pyramid(n):
    for i in range(1,n+1):
        if i == 1:
            pattern_list.append((n-i)*' '+i * '*'+ (n-i)*' ')
        else:
            pattern_list.append((n-i)*' '+i * '*' + (i-1)*'*'+(n-i)*' ')

    return pattern_list



def generate_pyramid(n):
    for i in range(n):
        stars = 2 * i + 1               # 1, 3, 5, ...
        spaces = n - i - 1              # leading spaces
        line = ' ' * spaces + '*' * stars
        print(line)
generate_pyramid(7)