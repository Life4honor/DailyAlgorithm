# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x_to_str = str(x)[::-1]
            return int(x_to_str) if int(x_to_str) < 2**31 else 0
        else:
            x_to_str = str(x)[1:][::-1]
            return 0 - int(x_to_str) if int(x_to_str) < 2**31 else 0


