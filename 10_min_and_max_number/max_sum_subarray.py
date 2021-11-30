# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def solution(nums):
    temp = max_total = nums[0]

    for item in nums[1:]:
        temp = max(item, item + temp)
        max_total = max(temp, max_total)

    return max_total
