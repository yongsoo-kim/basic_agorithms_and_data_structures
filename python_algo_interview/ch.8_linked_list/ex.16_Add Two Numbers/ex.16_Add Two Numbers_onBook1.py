# Quiz description URL:
#https://leetcode.com/problems/add-two-numbers/


# Point:
# 1. Convert to normal integers and sum them up.
# 2. Check the basic Python coding skills.

# Result
# Runtime: 76 ms, faster than 29.82% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 99.76% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결 리스트 뒤집기
    def reverseLists(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        list: List=[]
        while node:
            list.append(node.val)
            node = node.next
        return list


    #파이썬 리스트를 연결 리스트로 변환
    def toReverseLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None #이전 노드 정의
        for r in result:
            node = ListNode(r) # 새노드 생성
            node.next = prev # 이전노드의 next에 새 노드를 이어 붙임.
            prev = node # 현재노드를 이전노듸로 지정함.
        return node




    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        a = self.toList(self.reverseLists(l1))
        b = self.toList(self.reverseLists(l2))

        resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))

        return self.toReverseLinkedList(str(resultStr))