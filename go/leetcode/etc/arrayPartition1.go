// https://leetcode.com/problems/array-partition-i

func arrayPairSum(nums []int) int {
    sort.Ints(nums)
    length := len(nums)
    result := 0
    for i := 0; i < length; i+=2 {
        min := nums[i]
        if nums[i+1] < min {
           min = nums[i+1]
        }
        result += min
    }
    return result
}
