# Quiz description URL:
# https://leetcode.com/problems/two-sum/


# Point:
# Brutal force

# result
# Runtime: 3984 ms, faster than 5.04% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 8.83% of Python3 online submissions for Two Sum.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n =  len(nums)

        for i in range(0, n- 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

