# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def __init__(self):
        self.cache = []
        self.lps = ""

    def longestPalindrome(self, s: str) -> str:
        if s in self.cache:
            return
        self.cache.append(s)

        if self.isPalindrome(s):
            self.lps = s if len(s) > len(self.lps) else self.lps
        else:
            self.longestPalindrome(s[:-1])
            self.longestPalindrome(s[1:])

        return self.lps


    def isPalindrome(self, s: str):
        length = len(s)
        has_even_chars = length % 2 == 0

        index = length // 2
        return s[:index] == s[index:][::-1] if has_even_chars else s[:index] == s[index+1:][::-1]
