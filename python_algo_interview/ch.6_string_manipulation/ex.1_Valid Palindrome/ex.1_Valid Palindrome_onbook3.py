# Quiz description URL:
# https://leetcode.com/problems/valid-palindrome/

# Point:
# Use Slicing

# result
# Runtime: 32 ms, faster than 98.11% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.7 MB, less than 24.18% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        #정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]','',s)
        # s[::-1] (Slicing) will reverse the list! It's implemented in C, so very fast!
        return s == s[::-1] # This is slicing!

