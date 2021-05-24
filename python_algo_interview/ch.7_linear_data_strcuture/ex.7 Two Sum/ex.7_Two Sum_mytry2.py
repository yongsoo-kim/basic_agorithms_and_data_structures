# Quiz description URL:
# https://leetcode.com/problems/two-sum/


# Point:
# Use dict.

# result
# Runtime: 60 ms, faster than 16.16% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 6.48% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        n = len(nums)

        for i in range(n):
            num_dict[nums[i]] = i

        for j in range(n):
            diff = target - nums[j]
            if diff in num_dict.keys() and j != num_dict[diff]:
                return j, num_dict[diff]


