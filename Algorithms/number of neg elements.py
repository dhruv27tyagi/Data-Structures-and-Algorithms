"""
Description:
You are given an m x n matrix grid where each row and column is sorted in non-increasing order. 
Your task is to return the number of negative numbers present in the matrix.



Parameters:

grid (List[List[int]]): A 2D matrix with dimensions m x n, where each row and each column is sorted
in non-increasing order.

Return Values:

Integer: The count of negative numbers in the matrix.



Example:

Input: grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
Output: 7 
Explanation: There are 7 negative numbers in the matrix.
 
Input: grid = [[3, 2], [1, 0]] 
Output: 0 
Explanation: There are no negative numbers in the matrix.
"""

def countNegatives(grid):
    size_of_grid = len(grid)
    negative_numbers = 0
    for list in range(0,size_of_grid):
        size_of_list = len(grid[list])
        for element in range(0,size_of_list):
            if grid[list][element] < 0:
                negative_numbers +=1
            else:
                pass
    return negative_numbers

grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

print(countNegatives(grid=grid))

def countNegatives(self, grid):
    m, n = len(grid), len(grid[0])
    count = 0
    row, col = 0, n - 1

    while row < m and col >= 0:
        if grid[row][col] < 0:
                # All elements in this column below are negative, so count them
            count += m - row
            col -= 1  # Move left to the next column
        else:
            row += 1  # Move down to the next row
        
    return count