// https://www.hackerrank.com/challenges/grading/problem

func gradingStudents(grades []int32) []int32 {
    result := []int32{}
    for _, g := range(grades){
        if g < 38 {
            result = append(result, g)
            continue
        }
        m := g % 10
        if m < 5 {
            if 5 - m < 3 {
                g += 5 - m
            }
        } else {
            if 10 - m < 3 {
                g += 10 - m
            }
        }
        result = append(result, g)
    }
    return result
}
