// https://leetcode.com/problems/two-sum/submissions/

func twoSum(nums []int, target int) []int {
    result := []int{}
    lastIndex := len(nums)

    for i:=0; i<lastIndex; i++ {
        for j:= i+1; j<lastIndex; j++ {
            if nums[i] + nums[j] == target {
                result = append(result, i)
                result = append(result, j)
                return result
            }
        }
    }

    return result
}
