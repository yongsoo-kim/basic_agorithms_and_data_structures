# Quiz description URL:
# https://leetcode.com/problems/two-sum/


# Point:
# Upgraded version of onbook3.

# result
# Runtime: 56 ms, faster than 19.03% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 6.48% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
