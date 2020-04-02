# https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.recursive_climb(n)

    def recursive_climb(self, n: int, cache: dict = None):
        cache = {1:1, 2:2} if cache is None else cache
        if n in cache:
            return cache[n]

        cache[n] = self.recursive_climb(n - 1, cache) + self.recursive_climb(n - 2, cache)
        return cache[n]
