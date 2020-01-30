# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_cnt = {}

        for num in nums:
            try:
                nums_cnt[num] += 1
            except:
                nums_cnt[num] = 1

        result = sorted([num for num in nums_cnt], key = (lambda num: nums_cnt[num]), reverse = True)
        return result[:k]

