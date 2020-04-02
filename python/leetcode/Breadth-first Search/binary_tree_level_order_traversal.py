# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.queue = None
        self.dict = {}

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None

        self.traverse(node=root, level=0)
        return [self.dict[key] for key in self.dict if self.dict[key] != []][::-1]

    def traverse(self, node, level):
        if level not in self.dict:
            self.dict[level] = []

        if self.queue is None:
            self.queue = []

        self.dict[level].append(node.val)

        if node.left is not None:
            self.queue.append((level, node.left))

        if node.right is not None:
            self.queue.append((level, node.right))

        if self.queue == []:
            return

        level, node = self.queue.pop(0)
        self.traverse(node, level+1)

