# Quiz description URL:
#https://leetcode.com/problems/palindrome-linked-list/


# Point:
# 1.Use Multi-assignment
# 2.Use "Runner 기법"(Slow, Fast Runner)
# 3.솔직히 지금은 아직 이해가 잘 안간다!

# Result
# Runtime: 776 ms, faster than 78.50% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 31.5 MB, less than 95.52% of Python3 online submissions for Palindrome Linked List.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        #펠렌드롬 여부확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev

