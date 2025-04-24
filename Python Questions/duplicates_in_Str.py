"""
Remove Duplicates in a string
Problem Description:

You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string.

Input:

A single string s, where the length of s is between 1 and 1000.

Output:

A string that contains only the first occurrence of each character from the input string.

Example:

Input: "programming"
Output: "progamin"
 
Input: "Hello, World!"
Output: "Helo, Wrd!"

"""
def remove_duplicates(s):
    new_string = ''
    for char in s:
        
        if char not in new_string:
            new_string += char
            
    return new_string

print(remove_duplicates('programming code'))