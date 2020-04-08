// https://www.hackerrank.com/challenges/2d-array/problem

func hourglassSum(arr [][]int32) int32 {
    maximum_sum := int32(-63)

    for position_y := 0; position_y <= 3; {
        for position_x := 0; position_x <= 3; {
            current_sum := int32(0)

            selected := arr[position_y][position_x:position_x+3]
            for _, num := range(selected) {
                current_sum += num
            }

            current_sum += arr[position_y+1][position_x+1]

            selected = arr[position_y+2][position_x:position_x+3]
            for _, num := range(selected) {
                current_sum += num
            }
            if current_sum > maximum_sum {
                maximum_sum = current_sum
            }
            position_x += 1
        }
        position_y += 1
    }
    return maximum_sum
}
