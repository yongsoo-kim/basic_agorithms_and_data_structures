# Quiz description URL:
# https://leetcode.com/problems/array-partition-i/


# Point:
# 1. Sort it.
# 2. Use slicing for get "even number indexed value" -> Slicing is very fast!
# 2. In pair, always first element is smaller. So index number is even, that means it's first element. Sum it all.
#   ex) [1,2], [3, 4].... idx: 0, 2, ....
# result
# Runtime: 256 ms, faster than 84.79% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.8 MB, less than 84.65% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
