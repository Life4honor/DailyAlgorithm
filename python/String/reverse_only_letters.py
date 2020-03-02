# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = []
        non_alpha_index = {}
        for idx, char in enumerate(S):
            if char.isalpha():
                stack.append(char)
            else:
                non_alpha_index[idx] = char

        result = ""

        for idx in range(len(S)):
            if idx in non_alpha_index:
                result += non_alpha_index[idx]
            else:
                result += stack.pop()

        return result
