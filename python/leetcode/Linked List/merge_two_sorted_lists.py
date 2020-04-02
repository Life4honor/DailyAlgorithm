# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        initial = None
        node = None
        while l1 != None or l2 != None:
            if l1 == None:
                val = l2.val
                l2 = l2.next
            elif l2 == None:
                val = l1.val
                l1 = l1.next
            elif l1.val <= l2.val:
                val = l1.val
                l1 = l1.next
            elif l2.val < l1.val:
                val = l2.val
                l2 = l2.next

            if not node:
                node = ListNode(val)
                initial = node
            else:
                node.next = ListNode(val)
                node = node.next

        return initial
