# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        node = head
        while node is not None:
            stack.append(node.val)
            node = node.next

        new_head = None
        while len(stack) != 0:
            val = stack.pop()
            next_node = ListNode(val)
            if new_head is None:
                new_head = next_node
                cur_node = new_head
            else:
                cur_node.next = next_node
                cur_node = cur_node.next

        return new_head

