# Quiz description URL:
# https://leetcode.com/problems/valid-palindrome/


# Point:
# Use Deque.

# result
# Runtime: 52 ms, faster than 39.54% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 19.3 MB, less than 16.32% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use Deque
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            # Left pop is same as "pop(0)", but O(1). Much faster!
            if strs.leftpop() != strs.pop():
                return False

        return True
