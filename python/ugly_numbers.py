# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        now = 1
        l1_index, l2_index, l3_index = 0, 0, 0
        ugly_numbers = [1]
        while now < n:
            value1, value2, value3 = ugly_numbers[l1_index] * 2, ugly_numbers[l2_index] * 3, ugly_numbers[l3_index] * 5
            ugly_number = min(value1, value2, value3)
            ugly_numbers.append(ugly_number)

            if value1 == ugly_number:
                l1_index = l1_index + 1
            if value2 == ugly_number:
                l2_index = l2_index + 1
            if value3 == ugly_number:
                l3_index = l3_index + 1
            now = now + 1
        return ugly_numbers[-1]
