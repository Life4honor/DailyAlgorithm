// https://www.hackerrank.com/challenges/plus-minus/problem

func plusMinus(arr []int32) {
    positiveCnt := 0
    negativeCnt := 0
    zeroCnt := 0
    length := len(arr)

    for _, num := range(arr) {
        if (num > 0){
            positiveCnt += 1
        }
        if (num < 0){
            negativeCnt += 1
        }
        if (num ==0){
            zeroCnt += 1
        }
    }
    fmt.Printf("%f\n", float32(positiveCnt)/float32(length))
    fmt.Printf("%f\n", float32(negativeCnt)/float32(length))
    fmt.Printf("%f\n", float32(zeroCnt)/float32(length))
}
