// https://www.hackerrank.com/challenges/diagonal-difference/problem

func diagonalDifference(arr [][]int32) int32 {
    primaryDiagonal := 0
    secondaryDiagonal := 0
    for row, name := range(arr) {
        for column, num := range(name) {
            if (row == column){
                primaryDiagonal += int(num)
            }
            if (column == len(arr) - row - 1) {
                secondaryDiagonal += int(num)
            }
        }
    }

    if(primaryDiagonal >= secondaryDiagonal){
        return int32(primaryDiagonal - secondaryDiagonal)
    }

    return int32(secondaryDiagonal - primaryDiagonal)
}
