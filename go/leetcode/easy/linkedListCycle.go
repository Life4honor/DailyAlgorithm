// https://leetcode.com/problems/linked-list-cycle/

func hasCycle(head *ListNode) bool {
    if head == nil {
        return false
    }

    visited := make(map[*ListNode]bool)
    return hasCycleWithVisited(head.Next, visited)
}

func hasCycleWithVisited(head *ListNode, visited map[*ListNode]bool) bool {
    if head == nil {
        return false
    }

    if visited[head] {
        return true
    }
    visited[head] = true
    return hasCycleWithVisited(head.Next, visited)
}
