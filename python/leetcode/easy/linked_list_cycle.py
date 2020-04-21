# https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def __init__(self):
        self.visited = {}

    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        if head in self.visited:
            return True

        self.visited[head] = 1
        return self.hasCycle(head.next)
