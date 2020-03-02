# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alpha = []
        for char in s:
            if char.isalnum():
                only_alpha.append(char.lower())

        mid = len(only_alpha) // 2
        if len(only_alpha) % 2 == 0:
            return only_alpha[:mid] == only_alpha[mid:][::-1]
        else:
            return only_alpha[:mid] == only_alpha[mid+1:][::-1]
