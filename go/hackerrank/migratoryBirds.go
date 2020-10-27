# https://www.hackerrank.com/challenges/migratory-birds/problem

func migratoryBirds(arr []int32) int32 {
    types := map[int32]int32{1:0, 2:0, 3:0, 4:0, 5:0}
    for _, el := range arr {
        types[el] += 1
    }

    var result int32 = 1
    for t, v := range types {
        fmt.Println(t,v, types[result])
        if types[result] == v && t > result {
            continue
        }

        if (types[result] < v) {
            result = t
        }
    }

    return result
}