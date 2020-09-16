// https://www.hackerrank.com/challenges/apple-and-orange/problem

func countApplesAndOranges(s int32, t int32, a int32, b int32, apples []int32, oranges []int32) {
    h := map[int32]bool{}

    for i := s; i <= t; i++ {
        h[i] = true
    }

    ca:= 0
    for _, apple := range apples {
        if h[apple + a] {
            ca++
        }
    }
    fmt.Println(ca)

    co := 0
    for _, orange := range oranges {
        if h[orange + b] {
            co++
        }
    }
    fmt.Println(co)
}
