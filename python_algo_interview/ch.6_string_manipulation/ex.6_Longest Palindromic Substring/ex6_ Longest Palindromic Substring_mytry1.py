# Quiz description URL:
# https://leetcode.com/problems/longest-palindromic-substring/

# result
# Runtime: 7404 ms, faster than 17.61% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.4 MB, less than 37.39% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        for i in range(1, n):
            # i는 실행횟수
            for j in range(i):
                str_part = s[j:j + (n + 1 - i)]
                rev_str_part = str_part[::-1]

                if str_part == rev_str_part:
                    return str_part

        return s[0]



