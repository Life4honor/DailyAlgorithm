# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        node = root
        self.recursive_invert(node)
        return root

    def recursive_invert(self, node: TreeNode):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.recursive_invert(node.left)
        self.recursive_invert(node.right)
