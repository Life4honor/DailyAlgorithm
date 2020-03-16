# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def __init__(self):
        self.stack = []

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for value1 in nums1:
            self.stack.append(-1)
            for value2 in nums2[nums2.index(value1):]:
                if value2 > value1:
                    self.stack.pop()
                    self.stack.append(value2)
                    break

        return self.stack
