# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        head = None
        curr = ListNode()
        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next
        values.sort()

        for i, val in enumerate(values):
            curr.val = val
            if len(values) == 1:
                return ListNode(val)
            if i == len(values) - 1:
                curr.next = None
                return head
            if i == 0:
                curr.next = ListNode()
                head = curr
                curr = curr.next
            else:
                curr.next = ListNode()
                curr = curr.next
        return head

                
            