# Quiz description URL:
# https://leetcode.com/problems/product-of-array-except-self/


# Point:
# 1.Use math
# 2.Use slicing.

# result
# !!!!!Time Limit Exceeded!!!!!
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        result = []

        for i in range(0, n):
            arr = nums[:i] + nums[i + 1:]
            result.append(math.prod(arr))

        return result