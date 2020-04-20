// https://leetcode.com/problems/distribute-candies/

func distributeCandies(candies []int) int {
    my_candies := make(map[int]bool)
    ret := 0
    for _, candy := range(candies) {
        if !my_candies[candy] && affordable(ret, candies){
            ret++
        }
        my_candies[candy] = true
    }
    return ret
}

func affordable(ret int, candies []int) bool {
    return ret + 1 <= len(candies)/2
}
