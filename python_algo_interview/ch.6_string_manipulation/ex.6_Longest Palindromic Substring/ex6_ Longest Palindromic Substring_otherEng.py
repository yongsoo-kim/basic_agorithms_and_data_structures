# Quiz description URL:
# https://leetcode.com/problems/longest-palindromic-substring/
# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).

# point
# 1. Use 2 pointer.

# result
# Runtime: 284 ms, faster than 93.02% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.2 MB, less than 81.44% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]
