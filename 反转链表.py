# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        p = head
        cur = None
        pre = None
        while p is not None:
            cur = p.next
            p.next = pre
            pre = p
            p = cur
        return pre