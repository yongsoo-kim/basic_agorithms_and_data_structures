# Quiz description URL:
# https://leetcode.com/problems/array-partition-i/


# Point:
#1. Sort it.
#2. 인접요소 페어(Adjacent Element pairs) will be helpful.
#3. In pair, always first element is smaller. So index number is even, that means it's first element. Sum it all.
#   ex) [1,2], [3, 4].... idx: 0, 2, ....
# result
# Runtime: 264 ms, faster than 62.59% of Python3 online submissions for Array Partition I.
# Memory Usage: 16.8 MB, less than 84.65% of Python3 online submissions for Array Partition I.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수번째 값의 계산(array는 0부터 시작함 ex: 0, 2, 4...)
            if i % 2 == 0:
                sum += n

        return sum