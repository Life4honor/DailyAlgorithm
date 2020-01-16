# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        end_dict = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in end_dict and stack != []:
                last = stack.pop()
                if last != end_dict[char]:
                    return False
            else:
                stack.append(char)

        return stack == []
