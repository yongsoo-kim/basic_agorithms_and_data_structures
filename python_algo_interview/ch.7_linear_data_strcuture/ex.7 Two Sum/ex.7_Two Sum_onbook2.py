# Quiz description URL:
# https://leetcode.com/problems/two-sum/


# Point:
# 1. Use 'in'. Even though 'in' has O(n) complexity, it's faster than for loop!
# 2. Use slice[i+1:]:
# 3. Use index()

# result
# Runtime: 636 ms, faster than 5.16% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 10.59% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


