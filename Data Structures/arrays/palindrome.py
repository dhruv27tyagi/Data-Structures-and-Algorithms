"""
Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.

Input Parameters:

lst (List[int]): A list of integers.

Output:

bool: Return True if the list is a palindrome, otherwise False.
"""
def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # TODO: Implement this function
    last_number = -1

    for number in range(len(lst)):
        print(number)
        if lst[number] == lst[last_number]:
            number += 1
            last_number = last_number - 1
            return True
        else:
            return False


lst = [7, 8, 9, 8, 7]
print(is_palindrome(lst=lst))