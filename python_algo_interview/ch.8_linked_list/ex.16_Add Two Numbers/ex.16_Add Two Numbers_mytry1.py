# Quiz description URL:
#https://leetcode.com/problems/add-two-numbers/


# Point:
# 1. Convert to normal integers and sum them up.
# 2. Convert to Linked list.

# Result
# Runtime: 80 ms, faster than 18.24% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 70.30% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        arr1 = []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        arr2 = []
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        str1 = ""
        for i in arr1:
            str1 += str(i)

        str2 = ""
        for i in arr2:
            str2 += str(i)

        total = int(str1) + int(str2)

        total_str = str(total)

        arr3 = []

        for c in total_str:
            arr3.append(int(c))

        arr3 = arr3[::-1]

        arr4 = []
        for i in arr3:
            arr4.append(ListNode(i, None))

        head = arr4[0]
        result = head

        for i in range(1, len(arr4)):
            head.next = arr4[i]
            head = head.next

        return result