# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_reverse = []
        l2_reverse = []
        while l1 is not None:
            l1_reverse.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            l2_reverse.append(l2.val)
            l2 = l2.next

        l1_int = 0
        for idx, val in  enumerate(l1_reverse):
            l1_int += val * 10 ** idx

        l2_int = 0
        for idx, val in  enumerate(l2_reverse):
            l2_int += val * 10 ** idx


        result = str(l1_int + l2_int)[::-1]
        initial = ListNode(-1)
        node = initial
        for val in result:
            node.next = ListNode(val)
            node = node.next

        return initial.next
