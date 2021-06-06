# Quiz description URL:
#https://leetcode.com/problems/merge-two-sorted-lists/


# Point:
# 1.Use recursive
# 2.솔직히 이해가 잘 안간다...

# Result
# Runtime: 60 ms, faster than 5.15% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.5 MB, less than 29.08% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1