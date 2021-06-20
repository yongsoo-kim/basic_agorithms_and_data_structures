# Quiz description URL:
#https://leetcode.com/problems/swap-nodes-in-pairs/

# Point
# 1.Change the values only.(다소 변칙적임.)

# Result
# Runtime: 44 ms, faster than 11.96% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.4 MB, less than 14.07% of Python3 online submissions for Swap Nodes in Pairs.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 값만 바꾸기
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head