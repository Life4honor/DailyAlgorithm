# https://leetcode.com/problems/contains-duplicate/

from collections import defaultdict

class Solution:
    def __init__(self):
        self.cache = defaultdict(bool)

    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            if self.cache[num]:
                return True

            self.cache[num] = True

        return False

