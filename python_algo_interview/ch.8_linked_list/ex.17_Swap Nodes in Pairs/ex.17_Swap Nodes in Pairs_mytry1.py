# Quiz description URL:
#https://leetcode.com/problems/swap-nodes-in-pairs/

# Point:
# 1. Use dummy node for start!
# 더미노드를 head나 tail에 추가함으로서, head나 tail에서 작업해야하는 많은 edge케이스들을 다룰수 있게 된다.
# 더미노드의 존재는 필연적으로 작업이 head노드나 tail노드에서 행해지지 않아도 되는것을 보장하기에 null point체크같은 골치아픈 부분을 많이 해소해준다.

# Result
# Runtime: 24 ms, faster than 96.02% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 14.1 MB, less than 74.20% of Python3 online submissions for Swap Nodes in Pairs.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 더미노드로 이전 노드 정의. 스타트 포인트가 된다.
        #
        dummy = ListNode(0, head)
        prevNode = dummy
        currNode = head

        while currNode and currNode.next:
            secondNode = currNode.next
            nxtPtr = currNode.next.next
            # nxtPtr = secondNode.next

            secondNode.next = currNode
            currNode.next = nxtPtr
            prevNode.next = secondNode

            # 이순서는 끔찍하게 잘못되었다. 이동전에 "prev"를 지정해야하는데 그러지 않고 이동부터 해버렸다. 결과적으로 아래 라인에서 prev를 자기자신으로 지정하는 우를 범하고 말았다.
            #currNode = nxtPtr
            #prevNode = currNode

            #제대로 된 순서
            prevNode = currNode
            currNode = nxtPtr

        return dummy.next