"""
Count words in a string
Problem Description:

You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined as a sequence of characters separated by spaces.

Input:

A single string s, where the length of s is between 1 and 1000.

Output:

An integer representing the total count of words in the input string.

Example:

Input: "Hello, World!"
Output: 2
 
Input: "Python programming is fun."
Output: 4
"""

def count_words(s):
    #word_list = s.split()
    #word_count = len(word_list)

    #return word_count

    count = 0  # Initialize a counter for the number of words
    in_word = False  # Flag to track if we are inside a word
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is not a space
        if char != ' ':
            if not in_word:  # If we were not in a word before
                in_word = True  # Set the flag to indicate we are now in a word
                count += 1  # Increment the word count
        else:
            in_word = False  # If we encounter a space, we are not in a word anymore
    
    return count 

print(count_words('Python programming is fun.'))