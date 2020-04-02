# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = []
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.append(num)

        return result[0]
