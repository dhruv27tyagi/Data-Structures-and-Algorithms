"""
Description:
Given a list of integers, write a function to reverse the order of elements in the list.

Input Parameters:

lst (List[int]): A list of integers.

Output:

List[int]: The list with elements in reversed order.



Example:

Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
 
Input: lst = [10, 20, 30]
Output: [30, 20, 10]

"""

def reverse_list(lst):
    reversed_list = []
    idx = 0
    for number in range(len(lst)):
        idx = idx - 1
        reversed_list.append(lst[idx])
    return reversed_list

lst = [10, 20, 30,40]

print(reverse_list(lst=lst))