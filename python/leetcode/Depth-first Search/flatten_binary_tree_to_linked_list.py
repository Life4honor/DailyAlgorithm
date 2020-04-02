# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        visited = []
        stack = []
        initial = None

        node = root
        while node is not None:
            if node not in visited:
                if initial is None:
                    initial = TreeNode(root.val)
                    new_node = initial
                else:
                    new_node.right = TreeNode(node.val)
                    new_node = new_node.right
                visited.append(node)
                stack.append(node)

            if node.left is not None and node.left not in visited:
                node = node.left
            elif node.right is not None and node.right not in visited:
                node = node.right
            else:
                if stack == []:
                    break
                node = stack.pop()

        if initial is None:
            root = None
        else:
            root.left = initial.left
            root.right = initial.right

