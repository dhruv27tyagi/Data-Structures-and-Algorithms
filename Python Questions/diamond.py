"""
Diamond Pattern
Problem Description:

You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), 
and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.

Input:

A single integer n, where 1 <= n <= 100.

Output:

A list of strings where each string represents a row in the diamond pattern.

Example:

Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

"""

def generate_diamond(n):
    space = ' '
    diamond = []
    limit = n

    if n >=0:
        for i in range(n):
            element = space*(n-1) + (i+1)*'*' + space*(n-1)
            n -=1
            diamond.append(element)
    elif n < 0:
        
        for i in range(limit):
            element = space*(i+1) + (limit-1)*'*' + space*(i+1)
            limit -= 1
            diamond.append(element)

    return diamond

print(generate_diamond(3))