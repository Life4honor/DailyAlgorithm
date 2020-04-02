# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, n: int) -> str:
        alphabet = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        result = ""

        while n > 26:
            dividend, remainder = n // 26, n % 26
            result = alphabet[remainder] + result
            n = dividend if remainder != 0 else dividend -1

        result = alphabet[n % 26]+ result

        return result


