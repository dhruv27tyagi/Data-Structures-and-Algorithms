
def countNegatives(grid):
    """
    Count the number of negative numbers in a matrix sorted in non-increasing order
    both row-wise and column-wise using binary search.
    """
    def count_negatives_in_row(row):
        """
        Use binary search to count the number of negative numbers in a row.
        """
        left, right = 0, len(row)
        while left < right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid
            else:
                left = mid + 1
        return len(row) - left
    
    total_negatives = 0
    for row in grid:
        total_negatives += count_negatives_in_row(row)
    
    return total_negatives