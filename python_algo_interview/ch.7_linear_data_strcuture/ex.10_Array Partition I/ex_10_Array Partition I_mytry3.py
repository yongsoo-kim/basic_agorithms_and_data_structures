# Quiz description URL:
# https://leetcode.com/problems/array-partition-i/


# Point:
# 1. use sort and get every 2 nums.
# 2. Do not use min(), and always add up the first element from the pair.

# result
# Runtime: 264 ms, faster than 62.59% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.8 MB, less than 84.65% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        result = 0

        for i in range(0, len(nums) - 1, 2):
            result += nums[i]

        return result
