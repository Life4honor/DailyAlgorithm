# https://leetcode.com/problems/linked-list-cycle-ii/submissions/

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cache = []

        while head is not None and head not in cache:
            cache.append(head)
            head = head.next

        return head

# Another solution for 'Can you solve it without using extra space?'
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        while head is not None and head.val is not True:
            head.val = True
            head = head.next
                    
        return head
