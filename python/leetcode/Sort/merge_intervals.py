# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals, key=lambda interval:interval[0])

        prev_start_point, prev_end_point = [-1,-1]
        for interval in intervals:
            cur_start_point, cur_end_point = interval
            if cur_start_point <= prev_end_point:
                result.pop()
                cur_start_point = min([cur_start_point, prev_start_point])
                cur_end_point = max([cur_end_point, prev_end_point])

            result.append([cur_start_point, cur_end_point])
            prev_start_point, prev_end_point = cur_start_point, cur_end_point

        return result
