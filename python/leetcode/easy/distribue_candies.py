# https://leetcode.com/problems/distribute-candies/

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        me, my_candies_idx = [], {}
        for candy in candies:
            if candy not in my_candies_idx and len(me) + 1 <= len(candies) // 2:
                my_candies_idx[candy] = 1
                me.append(candy)

        return len(me)
