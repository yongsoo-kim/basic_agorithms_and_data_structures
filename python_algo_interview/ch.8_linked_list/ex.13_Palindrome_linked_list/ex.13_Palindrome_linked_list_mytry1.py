# Quiz description URL:
#https://leetcode.com/problems/palindrome-linked-list/


# Point:
# 1.Use Slicing
# 2.Last listNode's 'next' is None

# Result
# Runtime: 844 ms, faster than 38.93% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 47.1 MB, less than 47.57% of Python3 online submissions for Palindrome Linked List.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        val_list = []

        val_list.append(head.val)

        while head.next:
            head = head.next
            val_list.append(head.val)

        return val_list[:] == val_list[::-1]
