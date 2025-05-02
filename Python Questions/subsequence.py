"""
Check Subsequence
Problem Description:

You are given two strings s and t. Your task is to determine if string t is a subsequence of string s. 
A subsequence of a string is a new string that is formed from the original string by deleting some (or no) characters without changing the order of the remaining characters.

Input:
Two strings s and t where the length of s is between 1 and 1000, and the length of t is between 1 and 1000.

Output:
Return True if t is a subsequence of s, and False otherwise.

Example:

Input: s = "abcde", t = "ace"
Output: True
 
Input: s = "abcde", t = "aec"
Output: False
"""

def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s without using built-in functions.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    i, j = 0, 0  # Initialize two pointers for s and t
    
    # Loop through the original string s
    while i < len(s) and j < len(t):
        # If the characters match, move the pointer for t
        if s[i] == t[j]:
            j += 1
        # Always move the pointer for s
        i += 1
    
    # If we've matched all characters of t, return True
    return j == len(t)