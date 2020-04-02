# https://leetcode.com/problems/remove-linked-list-elements/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        while head is not None and head.val == val:
           head = head.next

        node = head
        while node is not None:
            while node.next is not None and node.next.val == val:
                node.next = node.next.next
            node = node.next

        return head
