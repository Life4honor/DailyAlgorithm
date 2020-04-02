# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = []
        while nums1 != [] and nums2 != []:
            if nums1[0] <= nums2[0]:
                new_list.append(nums1.pop(0))
            else:
                new_list.append(nums2.pop(0))

        if nums1 != []:
            new_list += nums1

        if nums2 != []:
            new_list += nums2

        length = len(new_list)
        mid = length // 2
        return new_list[mid] if length % 2 != 0 else (new_list[mid] + new_list[mid-1]) / 2
