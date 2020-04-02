# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.inspect(s) == self.inspect(t)

    def inspect(self, word):
        marker = 0
        map_to_int = {}
        for char in word:
            if char in map_to_int:
                continue

            map_to_int[char] = marker
            marker += 1

        return [map_to_int[char] for char in word]
