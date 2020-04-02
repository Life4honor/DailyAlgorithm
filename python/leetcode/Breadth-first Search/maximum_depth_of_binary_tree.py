# https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
        self.max_depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return self.max_depth

        self.bfs(root)
        return self.max_depth

    def bfs(self, node):
        self.initialize(node)

        if self.is_leaf(node):
            self.max_depth = max(self.max_depth, self.depth[node])

        if self.is_bfs_done():
            return

        if node.left is not None:
            self.queue.append(node.left)
            self.depth[node.left] = self.depth[node] + 1

        if node.right is not None:
            self.queue.append(node.right)
            self.depth[node.right] = self.depth[node] + 1

        node = self.queue.pop(0)
        return self.bfs(node)

    def initialize(self, node):
        if self.queue is None:
            self.queue = [node]
            self.depth[node] = 1

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def is_bfs_done(self):
        return self.queue == []

