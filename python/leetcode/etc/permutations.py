# https://leetcode.com/problems/permutations/

class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        root = Tree(None)

        self.connect_children(root, nums)
        self.traversal(root)

        return self.result

    def connect_children(self, node, nums):
        children = []
        nums = [num for num in nums if num != node.val]
        for num in nums:
            new_node = Tree(num)
            children.append(new_node)

        node.children = children
        for child in node.children:
            self.connect_children(child, nums)

    def traversal(self, node, result = []):
        result = copy.deepcopy(result)
        if node.val is not None:
            result.append(node.val)

        if node.children == []:
            self.result.append(result)
            return

        for child in node.children:
            self.traversal(child, result)

