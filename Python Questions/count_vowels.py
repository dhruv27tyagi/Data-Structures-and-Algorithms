"""
Count Vowels in a string
Problem Description:

You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count.

Input:

A single string s, where the length of s is between 1 and 1000.

Output:

An integer representing the total count of vowels in the input string.

Example:

Input: "Hello, World!"
Output: 3
 
Input: "Python Programming"
Output: 4
"""

def count_vowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for char in s:
        print(char)
        if char in vowels:
            count += 1
        
    return count

print(count_vowels('Helloo'))