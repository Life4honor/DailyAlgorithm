// https://leetcode.com/problems/average-of-levels-in-binary-tree/

func averageOfLevels(root *TreeNode) []float64 {
    level := 0
    elements := make(map[int][]int)
    result := make([]float64, 0)

    maxLevel := indexElements(root, level, elements)
    for i := 0; i < maxLevel; i++ {
        sum, length := 0, 0
        for _, el := range(elements[i]){
            sum += el
            length++
        }
        average := float64(sum) / float64(length)
        result = append(result, average)
    }
    return result
}

func indexElements(root *TreeNode, level int, elements map[int][]int) int {
    if root == nil {
        return level
    }

    elements[level] = append(elements[level], root.Val)
    level++

    left := indexElements(root.Left, level, elements)
    right := indexElements(root.Right, level, elements)
    if left > right {
        return left
    }
    return right
}
