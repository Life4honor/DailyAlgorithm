# https://leetcode.com/problems/majority-element/

class Solution:
    def __init__(self):
        self.count = {}

    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        max_count = 0
        for num in nums:
            if num not in self.count:
                self.count[num] = 0
            self.count[num] += 1

        for value, count in self.count.items():
            majority = value if max_count < count else majority
            max_count = max(max_count, count)

        return majority

