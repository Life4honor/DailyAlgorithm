// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

func findUnsortedSubarray(nums []int) int {
    alpha, omega, prev, max := 0, 0, nums[0], nums[0]
    alphaIsNotFound := true

    for idx, num := range(nums) {

        if alphaIsNotFound && prev > num {
            index, val := idx, num

            for index < len(nums) -1{
                if val > nums[index+1]{
                    val = nums[index+1]
                }
                index += 1
            }

            index = idx
            for index > 0 && nums[index-1] > val {
                index -= 1
            }

            alphaIsNotFound = false
            alpha = index
            omega = idx
        }
        prev = num

        if max <= num {
            max = num
        } else {
            omega = idx
        }

    }

    if alpha == omega {
        return 0
    }
    return omega - alpha + 1
}
