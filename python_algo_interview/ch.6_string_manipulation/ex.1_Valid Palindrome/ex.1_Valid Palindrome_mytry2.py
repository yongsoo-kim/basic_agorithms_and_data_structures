# Quiz description URL:
# https://leetcode.com/problems/valid-palindrome/


# My result.
#Runtime: 48 ms, faster than 57.74% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 19.6 MB, less than 13.13% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        alnum_list = list()

        for char in s:
            if char.isalnum():
                alnum_list.append(char.lower())

        n = len(alnum_list)

        mid_idx = n // 2

        for i in range(0, mid_idx):
            if alnum_list[i] == alnum_list[n - 1 - i]:
                continue
            else:
                return False

        return True

