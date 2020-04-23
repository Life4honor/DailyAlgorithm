# https://leetcode.com/problems/average-of-levels-in-binary-tree/

class Solution:
    def __init__(self):
        self.elements = {}

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        level = 0
        self.index_elements(root, level)

        for elements in self.elements.values():
            result.append(sum(elements)/len(elements))

        return result


    def index_elements(self, root: TreeNode, level: int):
        if root is None:
            return

        if level not in self.elements:
            self.elements[level] = []

        self.elements[level].append(root.val)
        level += 1

        self.index_elements(root.left, level)
        self.index_elements(root.right, level)
