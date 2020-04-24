# https://leetcode.com/problems/house-robber/

class Solution:
    def __init__(self):
        self.cache = {}

    def rob(self, nums: List[int]) -> int:
        return max(self.total_amount(nums, 0, 0), self.total_amount(nums, 1, 0))

    def total_amount(self, nums, position, total):
        if position >= len(nums):
            self.cache[position] = total
            return total

        if position in self.cache and self.cache[position] >= total:
            return self.cache[position]

        total += nums[position]

        return max(self.total_amount(nums, position+2, total), self.total_amount(nums, position+3, total))

