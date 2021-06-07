# Quiz description URL:
#https://leetcode.com/problems/reverse-linked-list/


# Point:
# Use stack for getting reversed order.

# Result
# Runtime: 56 ms, faster than 6.08% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 16.3 MB, less than 21.68% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        curr = head
        stack = []

        while curr:
            stack.append(ListNode(curr.val, None))
            curr = curr.next

        h_node = stack.pop()
        result = h_node

        while stack:
            t_node = stack.pop()
            h_node.next = t_node
            h_node = h_node.next

        return result
