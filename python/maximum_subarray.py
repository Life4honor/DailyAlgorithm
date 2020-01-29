# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        queue = []
        result = max(nums)
        for num in nums:
            queue.append(num)
            while sum(queue) < 0:
                if queue == []:
                    break
                queue.pop(0)

            result = max(result, sum(queue)) if queue != [] else result

        return result
