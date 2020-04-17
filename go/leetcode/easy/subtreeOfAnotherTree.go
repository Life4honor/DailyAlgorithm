// https://leetcode.com/problems/subtree-of-another-tree/

func isSubtree(s *TreeNode, t *TreeNode) bool {
    if s == nil {
        return false
    }

    leftSub, rightSub := s.Left, s.Right

    expected, expected_length := traverse(t)
    traversed, traversed_length := traverse(s)

    if isSameTree(expected, traversed) {
        return true
    }

    if expected_length < traversed_length {
        return isSubtree(leftSub, t) || isSubtree(rightSub, t)
    }

    return false
}

func traverse(tree *TreeNode) ([]int, int) {
    visited := make(map[*TreeNode]bool)
    stack := make([]*TreeNode, 0)
    stack = append(stack, tree)
    traversed := make([]int,0)

    node := tree
    for len(stack) > 0 {
        if node.Left != nil && !visited[node.Left] {
            visited[node.Left] = true
            stack = append(stack, node.Left)
            continue
        }

        if node.Right != nil && !visited[node.Right] {
            visited[node.Right] = true
            stack = append(stack, node.Right)
            continue
        }

        traversed = append(traversed, node.Val)
        node = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
    }

    return traversed, len(traversed)
}

func isSameTree(expected []int, traversed []int) bool {
    if len(expected) != len(traversed) {
        return false
    }

    for idx, val := range(expected){
        if val != traversed[idx] {
            return false
        }
    }
    return true
}
