# Quiz description URL:
#https://leetcode.com/problems/swap-nodes-in-pairs/



# Result
# Runtime: 28 ms, faster than 86.00% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.3 MB, less than 46.17% of Python3 online submissions for Swap Nodes in Pairs.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 더미노드로 이전 노드 정의. 스타트 포인트가 된다.
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            nextPair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nextPair
            prev.next = second

            prev = curr
            curr = nextPair

        return dummy.next