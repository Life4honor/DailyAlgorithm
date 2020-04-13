# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0

        while nums != []:
            first = nums.pop()
            second = nums.pop()
            result += min(first, second)

        return result
