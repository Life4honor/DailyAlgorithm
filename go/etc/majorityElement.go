// https://leetcode.com/problems/majority-element/

func majorityElement(nums []int) int {
    var valueCount = make(map[int]int)

    for _, value := range nums {
        valueCount[value] += 1
    }

    resultCount := -1
    result := -1

    for key, count := range valueCount {
        if count > resultCount {
            resultCount = count
            result = key
        }
    }
    return result
}
