# Quiz description URL:
# https://leetcode.com/problems/reverse-string/

# Point:
# Use copy and slicing

# result
# Runtime: 204 ms, faster than 23.31% of Python3 online submissions for Reverse String.
# Memory Usage: 18.5 MB, less than 94.60% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

        # This does not work. This is leetcode platform issue. Normally, this should work.
        # s = s[::-1]


