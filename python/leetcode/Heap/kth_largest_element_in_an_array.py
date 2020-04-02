# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        target_idx = size - k

        return sorted(nums)[target_idx]

