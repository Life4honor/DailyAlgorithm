# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        expected = r*c

        cur_col = len(nums)
        cur_row = len(nums[0])

        if cur_col * cur_row != expected:
            return nums

        result = []
        new_row = []
        for row in nums:
            for el in row:
                new_row.append(el)
                if len(new_row) == c:
                    result.append(new_row)
                    new_row = []

        return result
