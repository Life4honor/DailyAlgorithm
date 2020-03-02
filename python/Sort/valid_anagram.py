# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        cnt_char = {}
        for char in s:
            if char not in cnt_char:
                cnt_char[char] = 1
            else:
                cnt_char[char] += 1

        for char in t:
            if char not in cnt_char:
                return False
            else:
                cnt_char[char] -= 1

        keys = [key for key in cnt_char]
        for key in keys:
            if cnt_char[key] != 0:
                return False
        return True

