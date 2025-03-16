"""
Given a list of integers, write a function to find the maximum element in the list.

Input Parameters:

lst (List[int]): A list of integers.

Output:

int: The maximum element in the list.


Example:

Input: lst = [3, 5, 2, 9, 6]
Output: 9
 
Input: lst = [-1, -2, -3, -4]
Output: -1
 
Input: lst = [7]
Output: 7
"""
def find_max_element(lst):
    max_number = lst[0]
    for number in lst:
        if number > max_number:
            max_number = number
        
    return max_number

lst = [3, 5, 2, 9,34, 6]
print(find_max_element(lst=lst))
