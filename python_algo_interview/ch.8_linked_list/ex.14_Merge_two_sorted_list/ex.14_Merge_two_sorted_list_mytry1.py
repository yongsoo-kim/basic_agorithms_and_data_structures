# Quiz description URL:
#https://leetcode.com/problems/merge-two-sorted-lists/


# Point:
# 1.It is almost like merge sort.

# Result
# Runtime: 40 ms, faster than 46.60% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.3 MB, less than 60.45% of Python3 online submissions for Merge Two Sorted Lists.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(-1)
        ret = head;

        while (l1 and l2):
            v1 = l1.val
            v2 = l2.val

            if v1 <= v2:
                ret.next = l1
                l1 = l1.next
            else:
                ret.next = l2
                l2 = l2.next

            ret = ret.next

        if l1 is None:
            ret.next = l2
        else:
            ret.next = l1

        return head.next