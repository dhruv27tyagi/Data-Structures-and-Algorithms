"""
Check for same strings
Problem Description:

You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.

Input:

Two strings s and t, where 1 <= len(s), len(t) <= 1000.

Output:

A boolean value (True or False) indicating whether the two strings are equal.

Example:

Input: s = "hello", t = "hello"
Output: True
 
Input: s = "hello", t = "world"
Output: False

"""
def check_duplicate(s,t):
    #if s[::-1] == t[::-1]:
    #    return True
    #else:
    #    return False
    len_s = 0
    len_t = 0
    
    # Calculate lengths of both strings manually
    while len_s < len(s):
        len_s += 1
    while len_t < len(t):
        len_t += 1
    
    # If lengths are not equal, the strings can't be equal
    if len_s != len_t:
        return False
    
    # Compare characters one by one
    for i in range(len_s):
        if s[i] != t[i]:
            return False  # If a character doesn't match, return False
 
    return True  
print(check_duplicate('hello','hello'))