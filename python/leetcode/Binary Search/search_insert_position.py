# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = None

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while position is None:
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                position = mid

            if right - left <= 1:
                if nums[left] >= target:
                    position = left
                elif nums[right] >= target:
                    position = right
                else:
                    position = right + 1

            mid = (left + right) // 2

        return position
