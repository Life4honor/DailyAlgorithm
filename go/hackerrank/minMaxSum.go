// https://www.hackerrank.com/challenges/mini-max-sum/problem

func miniMaxSum(arr []int32) {
    min := int32(-1)
    max := int32(-1)
    sum := int32(0)

    for _, el := range arr {
        sum += el
        if (min < 0 || min > el){
            min = el
        }
        if (max < 0 || max < el){
            max = el
        }
    }
    fmt.Println(sum - max, sum - min)
}
