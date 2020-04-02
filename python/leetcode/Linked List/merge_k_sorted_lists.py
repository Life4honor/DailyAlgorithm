# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        result = self.mergeLists(lists)

        return result

    def mergeLists(self, lists: List[ListNode]):
        if len(lists) == 1:
            return lists[0]

        if len(lists) == 0:
            return None

        new_lists = ListNode(None)
        root = new_lists
        first_list = lists.pop()
        second_list = lists.pop()

        while first_list is not None and second_list is not None:
            if first_list.val <= second_list.val:
                new_lists.next = first_list
                first_list = first_list.next
            else:
                new_lists.next = second_list
                second_list = second_list.next

            new_lists = new_lists.next

        if first_list is not None:
            new_lists.next = first_list
        else:
            new_lists.next = second_list

        lists.append(root.next)

        return self.mergeLists(lists)

