# Quiz description URL:
# https://leetcode.com/problems/valid-palindrome/


# My result.
# Runtime: 552 ms, faster than 5.21% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 25.5 MB, less than 6.17% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        queue = list()
        stack = list()

        for char in s:
            if char.isalpha() or char.isnumeric():
                queue.append(char.lower())
                stack.append(char.lower())

        qn = len(queue)

        for i in range(qn):
            if queue.pop(0) == stack.pop():
                continue
            else:
                return False

        return True
