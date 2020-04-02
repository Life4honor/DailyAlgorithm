# https://leetcode.com/problems/happy-number/

class Solution:
    def __init__(self):
        self.cache = []

    def isHappy(self, n: int) -> bool:
        if n in self.cache:
            return False

        self.cache.append(n)
        if n == 1:
            return True

        nums = self.split(n)
        square_value = self.square_value(nums)
        return self.isHappy(square_value)

    def split(self, n: int) -> list:
        n_to_str = str(n)
        return [int(num) for num in n_to_str]

    def square_value(self, nums: list):
        square_value = 0
        for num in nums:
            square_value += num ** 2
        return square_value
