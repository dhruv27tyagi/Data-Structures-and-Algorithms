"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Input Parameters:

nums (List[int]): A list of integers where each integer is unique and in the range [0, n].

Output:

int: The missing number in the range [0, n].


Example:

Input: nums = [3, 0, 1]
Output: 2
 
Input: nums = [0, 1]
Output: 2
 
Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
Output: 5

"""

def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    # TODO: Implement this function
    for i in range(max(nums)+1):
        if i not in nums:
            return i
    return max(nums)+1
        
nums = [0,1]

print(find_missing_number(nums=nums))