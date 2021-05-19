# Quiz description URL:
# https://leetcode.com/problems/reverse-string/

# result
# Runtime: 200 ms, faster than 37.80% of Python3 online submissions for Reverse String.
# Memory Usage: 18.5 MB, less than 94.60% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        mid_idx = n // 2

        for i in range(mid_idx):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]



