# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        values = []
        for char in s:
            values.append(roman_value[char])

        result = 0
        while values != []:
            current_value = values.pop()
            if values == []:
                result += current_value
                break

            if current_value in (5, 10) and values[-1] == 1:
                result += current_value - values.pop()
                continue

            if current_value in (50, 100) and values[-1] == 10:
                result += current_value - values.pop()
                continue

            if current_value in (500, 1000) and values[-1] == 100:
                result += current_value - values.pop()
                continue

            result += current_value

        return result
