"""Maximum Element in a List.

Description:
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

def max_element(lst):

    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element

    return max_element

print(max_element([-6, -2, -3, -4]))