# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_idx = 0
        while first_idx < len(nums) - 1:
            first_element = nums[first_idx]

            for idx, num in enumerate(nums[first_idx + 1:]):
                if first_element + num == target:
                    return [first_idx, first_idx + idx + 1]

            first_idx += 1
        return None
