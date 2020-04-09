// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

func rotLeft(a []int32, d int32) []int32 {
    length := int32(len(a))
    move := d % length
    left := a[move:]
    right := a[:move]

    result := make([]int32, length, length)
    index := 0
    for _, num := range(left) {
        result[index] = num
        index += 1
    }

    for _, num := range(right) {
        result[index] = num
        index += 1
    }

    return result
}
