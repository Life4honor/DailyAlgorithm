// https://www.hackerrank.com/challenges/ctci-ransom-note/problem

func checkMagazine(magazine []string, note []string) {
    m := make(map[string]int)

    for _, word := range(magazine){
        m[word] += 1
    }

    for _, word := range(note){
        if exist := m[word]; exist == 0 {
            fmt.Print("No")
            return
        }

        m[word] -= 1
        if m[word] < 0 {
            fmt.Print("No")
            return
        }
    }

    fmt.Print("Yes")
    return
}
