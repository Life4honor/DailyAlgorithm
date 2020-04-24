// https://leetcode.com/problems/house-robber/

func rob(nums []int) int {
    cache := make(map[int]int)

    totalAmount(nums, cache, 0, 0)
    totalAmount(nums, cache, 1, 0)

    result := 0
    for _, total := range(cache){
        if total > result {
            result = total
        }
    }
    return result
}

func totalAmount(nums []int, cache map[int]int, position int, total int) {
    if position >= len(nums){
        if cache[position] < total{
            cache[position] = total
        }
        return
    }
    total += nums[position]
    totalAmount(nums, cache, position+2, total)
    totalAmount(nums, cache, position+3, total)
}


