# Quiz description URL:
#https://leetcode.com/problems/palindrome-linked-list/


# Point:
# 1.Use list

# Result
# Runtime: 2612 ms, faster than 5.00% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 47.3 MB, less than 37.11% of Python3 online submissions for Palindrome Linked List.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        q: List = []

        if not head:
            return True

        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # Palindrome check
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True
