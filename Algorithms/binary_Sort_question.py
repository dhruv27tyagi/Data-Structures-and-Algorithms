"""

Description:
You are given a sorted array of characters letters, sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
Your task is to return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Input:

letters: A sorted array of characters in non-decreasing order.

target: A character to compare against.

Output:

Return the smallest character that is greater than target. If no such character exists, return the first character in letters.


Example:

Input:
letters = ['c', 'f', 'j']
target = 'k'
Output: 'c'
 
Input:
letters = ['c', 'f', 'j']
target = 'c'
Output: 'f'
 
Input:
letters = ['c', 'f', 'j']
target = 'a'
Output: 'c'

"""

def next_greatest_letter(letters, target):
    left, right = 0, len(letters)

    while left < right:
        mid= left + (right - left)//2

        if letters[mid] > target:
            
            right = mid
        else:
            left = mid + 1
            
    return letters[left % len(letters)]

letters = ['c', 'f', 'j','l','q','s']

print(next_greatest_letter(letters=letters, target = 'o'))
        