# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = []
        result = -1 if len(s) > 0 else 0

        for char in s:
            if char not in cache:
                cache.append(char)
            else:
                cache = cache[cache.index(char) + 1:]
                cache.append(char)

            result = max(len(cache), result)

        return result
