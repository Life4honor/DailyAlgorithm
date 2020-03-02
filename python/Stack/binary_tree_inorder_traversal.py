# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # left -> current -> right : inorderTraversal
        result = []
        stack = []
        node = root
        while node is not None:
            if node.left is not None and node.left not in result:
                stack.append(node)
                node = node.left
                continue

            if node not in result:
                result.append(node)
                if node.right is not None and node.right not in result:
                    node = node.right
                    continue

                if stack != []:
                    node = stack.pop()
                    continue

            return [el.val for el in result]
