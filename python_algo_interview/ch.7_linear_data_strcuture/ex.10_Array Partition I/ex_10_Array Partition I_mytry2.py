# Quiz description URL:
# https://leetcode.com/problems/array-partition-i/


# Point:
# 1. Find the biggest and 2nd biggest.
# !!!! But sort gives us "O(NlogN)"!!!!!!!!!

# result
#!!!!!!!!!!Time Limit Exceeded!!!!!!!!!!!
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0

        while nums:   # O(N)
            v1 = max(nums)
            nums.remove(v1) # O(N). So... This with line No.15, this will make O(N^2)

            v2 = max(nums)
            nums.remove(v2)

            result += min(v1, v2)

        return result
