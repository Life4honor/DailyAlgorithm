// https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

func breakingRecords(scores []int32) []int32 {

    var (
        breakMaxCount, breakMinCount int32
    )

    init := true
    var max, min int32

    for _, score := range(scores) {
        if init {
            max, min = score, score
            init = false
        }

        if score > max {
            max = score
            breakMaxCount += 1
        }

        if score < min {
            min = score
            breakMinCount += 1
        }

    }

    return []int32{breakMaxCount, breakMinCount}
}