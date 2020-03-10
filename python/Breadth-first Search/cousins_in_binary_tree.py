# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.queue = None
        self.depth = {}
        self.parent = {}

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.bfs(root)

        if self.depth[x] == self.depth[y] and self.parent[x] != self.parent[y]:
            return True

        return False

    def bfs(self, node):
        if self.queue == []:
            return

        if self.queue is None:
            self.queue = [node]
            self.depth[node.val] = 0
            self.parent[node.val] = None

        if node is None:
            return

        depth = self.depth[node.val]

        if node.left is not None:
            self.queue.append(node.left)
            self.depth[node.left.val] = depth+1
            self.parent[node.left.val] = node

        if node.right is not None:
            self.queue.append(node.right)
            self.depth[node.right.val] = depth+1
            self.parent[node.right.val] = node

        node = self.queue.pop(0)
        self.bfs(node)

