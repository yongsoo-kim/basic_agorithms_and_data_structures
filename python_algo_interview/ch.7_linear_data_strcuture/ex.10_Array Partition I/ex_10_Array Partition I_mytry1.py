# Quiz description URL:
# https://leetcode.com/problems/array-partition-i/


# Point:
# 1. use sort and get every 2 nums.
# !!!! But sort gives us "O(NlogN)"!!!!!!!!!

# result
# Runtime: 280 ms, faster than 26.07% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.5 MB, less than 98.82% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        result = 0

        for i in range(0, len(nums) - 1, 2):
            result +=  nums[i + 1]

        return result
