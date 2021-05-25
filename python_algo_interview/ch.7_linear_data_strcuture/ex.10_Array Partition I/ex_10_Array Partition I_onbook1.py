# Quiz description URL:
# https://leetcode.com/problems/array-partition-i/


# Point:
#1. Sort it.
#2. 인접요소 페어(Adjacent Element pairs) will be helpful.

# result
# Runtime: 264 ms, faster than 62.59% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.8 MB, less than 84.65% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            # 앞에서부터 오름차운으로 페어를 만들어서 합계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum