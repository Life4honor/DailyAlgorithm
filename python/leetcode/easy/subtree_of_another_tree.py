# https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False

        left_sub, right_sub = s.left, s.right

        expected, expected_length = self.traverse(t)
        traversed, traversed_length = self.traverse(s)

        if expected == traversed:
            return True

        if expected_length < traversed_length:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        return False

    def traverse(self, tree: TreeNode):
        if tree is None:
            return tree

        stack = [tree]
        visited = {}
        traversal = []

        node = stack[0]
        while stack != []:
            if node.left is not None and node.left not in visited:
                visited[node.left] = 1
                stack.append(node.left)
                continue

            if node.right is not None and node.right not in visited:
                visited[node.right] = 1
                stack.append(node.right)
                continue

            traversal.append(node.val)
            node = stack.pop()

        return traversal, len(traversal)
