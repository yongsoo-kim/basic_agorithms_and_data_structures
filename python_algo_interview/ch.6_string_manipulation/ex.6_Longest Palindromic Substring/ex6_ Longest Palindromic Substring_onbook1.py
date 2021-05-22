# Quiz description URL:
# https://leetcode.com/problems/longest-palindromic-substring/


# point
# 1. Use 2 pointer.
# !!!!!!!!!!!!!!!!!!! But this is hard to understand!!!!!!!!!!!!!!!!!!!!!

# result
# Runtime: 284 ms, faster than 93.02% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.2 MB, less than 81.44% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 펠렌드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1: right - 1]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)

        return result
