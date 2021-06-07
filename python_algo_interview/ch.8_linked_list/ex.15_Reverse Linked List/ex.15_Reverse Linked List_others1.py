# Quiz description URL:
#https://leetcode.com/problems/reverse-linked-list/


# Point:
# 1. Think about the meaning of "curr.next = prev"... It is changing the direction!
# 2. Drawing nodes will be helpful.

# Result
# Runtime: 36 ms, faster han 65.02% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.6 MB, less than 74.63% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize pointers

        prev = None
        curr = head
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
