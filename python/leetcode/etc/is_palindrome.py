# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = str(x)
        mid_idx = len(x) // 2
        if len(x) % 2 == 0:
            left = x[:mid_idx]
            right = x[mid_idx:][::-1]
        else:
            left = x[:mid_idx]
            right = x[mid_idx+1:][::-1]

        return left == right


