# Quiz description URL:
# https://leetcode.com/problems/reverse-string/

# Point:
# Use 2 pointers.

# result
# Runtime: 188 ms, faster than 87.68% of Python3 online submissions for Reverse String.
# Memory Usage: 18.6 MB, less than 59.02% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
