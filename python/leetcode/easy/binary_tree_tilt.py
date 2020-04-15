# https://leetcode.com/problems/binary-tree-tilt/

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self.tilt_of_node(root) + self.findTilt(root.left) + self.findTilt(root.right)


    def tilt_of_node(self, node: TreeNode):
        if node is None:
            return 0

        left, right = node.left, node.right

        left_sum = self.total_sum_of_tree(left)
        right_sum = self.total_sum_of_tree(right)
        return abs(left_sum - right_sum)

    def total_sum_of_tree(self, root):
        if root is None:
            return 0

        ret = 0
        visited = {}
        stack = [root]

        while stack != []:
            node = stack[-1]
            visited[node] = True
            if node.left is not None and node.left not in visited:
                stack.append(node.left)
                continue
            if node.right is not None and node.right not in visited:
                stack.append(node.right)
                continue
            ret += node.val
            stack.pop()

        return ret

