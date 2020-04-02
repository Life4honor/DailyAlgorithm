# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.initialize_fields()

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.tree_traversal(p)
        traversed_p = self.traversal_order, self.traversal_direction

        self.initialize_fields()

        self.tree_traversal(q)
        traversed_q = self.traversal_order, self.traversal_direction

        return traversed_p == traversed_q

    def tree_traversal(self, tree: TreeNode):
        if tree is None:
            return
        self.traversal_order.append(tree.val)
        if tree.left is not None:
            self.stack.append(tree)
            self.traversal_direction.append("left")
            self.tree_traversal(tree.left)
        elif tree.right is not None:
            self.traversal_direction.append("right")
            self.tree_traversal(tree.right)
        else:
            self.traversal_direction.append("pop")
            if self.stack == []:
                return
            tree = self.stack.pop()

            while tree.right is None:
                if self.stack == []:
                    break
                tree = self.stack.pop()

            self.tree_traversal(tree.right)

    def initialize_fields(self):
        self.traversal_order = []
        self.traversal_direction = []
        self.stack = []
