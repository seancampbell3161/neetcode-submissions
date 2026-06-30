# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, curr, prev):
        if curr is None:
            return prev
        new = curr.next
        curr.next = prev
        prev = curr
        return self.reverse(new, prev)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)