# https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        size = 0
        node = head
        while node is not None:
            size += 1
            node = node.next

        mid = size // 2

        for _ in range(mid):
            head = head.next

        return head
