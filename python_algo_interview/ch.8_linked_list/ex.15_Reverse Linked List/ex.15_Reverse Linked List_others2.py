# Quiz description URL:
#https://leetcode.com/problems/reverse-linked-list/


# Point:
# 1. Use recursive
# 2. 'reversedListHead' is always the last node.

# Result
# Runtime: 32 ms, faster than 86.77% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 18.9 MB, less than 14.83% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        reversedListHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reversedListHead
