# Quiz description URL:
# https://leetcode.com/problems/trapping-rain-water/


# Point:
# 1. Use 2 pointers.

# result
# Runtime: 44 ms, faster than 97.18% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 14.9 MB, less than 63.84% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:

            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


