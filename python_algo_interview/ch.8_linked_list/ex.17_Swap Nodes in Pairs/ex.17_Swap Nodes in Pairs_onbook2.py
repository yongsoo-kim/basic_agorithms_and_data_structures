# Quiz description URL:
#https://leetcode.com/problems/swap-nodes-in-pairs/

# Point
# 1.재귀로 스왑하는 방법.
# 2.더미 노드가 필요없기때문에 더 깔끔함.

# Result
# Runtime: 32 ms, faster than 64.02% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.2 MB, less than 74.09% of Python3 online submissions for Swap Nodes in Pairs.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
