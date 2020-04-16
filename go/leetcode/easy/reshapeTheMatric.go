// https://leetcode.com/problems/reshape-the-matrix/

func matrixReshape(nums [][]int, r int, c int) [][]int {
    result := make([][]int, 0)
    new_row := make([]int, 0)

    if r*c != len(nums[0]) * len(nums) {
        return nums
    }

    for _, row := range nums {
        for _, el := range row {
            new_row = append(new_row, el)
            if len(new_row) == c {
                result = append(result, new_row)
                new_row = make([]int, 0)
            }
        }
    }

    return result
}
