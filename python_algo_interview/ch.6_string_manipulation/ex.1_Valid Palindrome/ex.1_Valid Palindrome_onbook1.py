# Quiz description URL:
# https://leetcode.com/problems/valid-palindrome/


# result
# Runtime: 292 ms, faster than 5.21% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 19.6 MB, less than 10.07% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())


        while len(strs) > 1:
            # pop(0) costs O(n), so List will cost us O(n^2)
            if strs.pop(0) != strs.pop():
                return False

        return True
