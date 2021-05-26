# Quiz description URL:
# https://leetcode.com/problems/product-of-array-except-self/


# Point:
# 1.Think left and right separately.
# 2. "1" can be multiplied and it won't affect number change. Let's use this number for default number.

# result
# Runtime: 264 ms, faster than 13.57% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.9 MB, less than 27.13% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        p = 1
        out1 = []
        for i in range(0, n):
            if i == 0:
                out1.append(1)
            else:
                p = p * nums[i - 1]
                out1.append(p)

        p = 1
        out2 = []
        for j in range(n - 1, -1, -1):
            if j == n - 1:
                out2.append(1)
            else:
                p = p * nums[j + 1]
                out2.append(p)

        out2 = out2[::-1]

        result = []
        for f in range(0, n):
            product = out1[f] * out2[f]
            result.append(product)

        return result