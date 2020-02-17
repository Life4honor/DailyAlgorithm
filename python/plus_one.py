# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        power = 0
        while digits != []:
            result += digits.pop() * 10**power
            power += 1

        result = [el for el in str(result + 1)]
        return result
