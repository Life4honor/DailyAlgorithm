# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cache = []
        node = head

        if head is None:
            return head
        
        while node is not None:
            cache.append(node.val)
            while node.next is not None and node.next.val in cache:
                node.next = node.next.next
            node = node.next
        
        return head
