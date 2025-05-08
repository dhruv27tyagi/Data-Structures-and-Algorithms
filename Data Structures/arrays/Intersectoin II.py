"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
def intersect(nums1, nums2):
    freq1 = {}
    result = []

    # Build frequency map for nums1
    for num in nums1:
        if num in freq1:
            freq1[num] += 1
        else:
            freq1[num] = 1

    # Traverse nums2 and collect common elements
    for num in nums2:
        if num in freq1 and freq1[num] > 0:
            result.append(num)
            freq1[num] -= 1

    return result



nums1 = [2,3,3,4,5,5,2]
nums2 = [3,3,5]

print(intersect(nums1=nums1, nums2=nums2))