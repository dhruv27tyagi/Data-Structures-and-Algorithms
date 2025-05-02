"""
Check for anagrams
Problem Description:

You are given two strings s and t. Your task is to determine if string t is an anagram of string s. An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, 
using all the original characters exactly once.

Input:

Two strings s and t where both lengths are between 1 and 1000.

Output:

Return True if t is an anagram of s, and False otherwise.

Example:

Input: s = "anagram", t = "nagaram"
Output: True
 
Input: s = "rat", t = "car"
Output: False
"""

def is_anagram(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)