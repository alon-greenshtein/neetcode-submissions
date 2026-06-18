# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if not head.next.next:
            head.next.next = head
            tmp = head.next
            head.next = None
            return tmp
        
        n0 = head
        n1 = n0.next
        n2 = n1.next
        n0.next = None
        while n2:
            n1.next = n0
            n0 = n1
            n1 = n2
            n2 = n2.next
        n1.next = n0
        return n1

        