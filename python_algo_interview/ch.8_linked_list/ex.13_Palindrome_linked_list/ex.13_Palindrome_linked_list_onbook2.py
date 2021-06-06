# Quiz description URL:
#https://leetcode.com/problems/palindrome-linked-list/


# Point:
# 1.Use Deque

# Result
# Runtime: 992 ms, faster than 11.86% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.9 MB, less than 53.90% of Python3 online submissions for Palindrome Linked List.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        q: Deque = collections.deque()

        if not head:
            return True

        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # Palindrome check
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True
