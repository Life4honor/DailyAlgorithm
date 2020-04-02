# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        target = head
        new_node = ListNode(None)
        head = new_node

        for _ in range(n):
            node = node.next

        while node is not None:
            new_node.next = ListNode(target.val)
            new_node = new_node.next

            node = node.next
            target = target.next

        new_node.next = target.next
        return head.next
