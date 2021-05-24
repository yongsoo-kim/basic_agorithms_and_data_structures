# Quiz description URL:
# https://leetcode.com/problems/two-sum/


# Point:
# Brutal force

# result
# Runtime: 4024 ms, faster than 5.00% of Python3 online submissions for Two Sum.
# Memory Usage: 14.7 MB, less than 12.00% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


