# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.queue = []

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.queue.append((1, root))
        grouped_by_depth = {}

        while self.queue != []:
            current_depth, current_node = self.queue.pop(0)

            if current_depth not in grouped_by_depth:
                grouped_by_depth[current_depth] = []

            if current_node is None:
                grouped_by_depth[current_depth].append(None)
                continue

            grouped_by_depth[current_depth].append(current_node)
            self.queue.append((current_depth + 1, current_node.left))
            self.queue.append((current_depth + 1, current_node.right))

        min_depth = None

        for depth, values in grouped_by_depth.items():
            if True in [self.is_leaf(value) for value in values]:
                min_depth = min(min_depth, depth) if min_depth is not None else depth

        return min_depth

    def is_leaf(self, node):
        if node is None:
            return node

        return node.left is None and node.right is None
