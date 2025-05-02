"""
Check for Substring
Problem Description:

You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s.
 A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for string operations and do not use recursion.

Input:
Two strings s and t, where 1 <= len(s), len(t) <= 1000.

Output:
A boolean value (True or False) indicating whether t is a substring of s.

Example:

Input: s = "hello world", t = "world"
Output: True
 
Input: s = "hello world", t = "worlds"
Output: False

"""

def is_substring(s,t):
    if len(t) == 0:
        return True
    s = s.split()
    
    if t in s:
        return True

    else:
        return False

print(is_substring(s="hello world",t = "worlds"))