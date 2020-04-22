# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        alpha, omega = 0, 0
        prev, max_, min_ = nums[0], nums[0], None
        alpha_is_not_found = True

        for idx, num in enumerate(nums):
            if alpha_is_not_found and prev > num:
                min_ = num
                alpha = idx
                alpha_is_not_found = False

                while alpha+1 < len(nums):
                    min_ = min(min_, nums[alpha+1]) if min_ is not None else nums[alpha+1]
                    alpha += 1

                alpha = idx
                while alpha > 0 and min_ < nums[alpha-1]:
                    alpha -= 1

            if max_ <= num:
                max_ = num
            else:
                omega = idx

            prev = num
        return omega - alpha + 1 if omega != alpha else 0
