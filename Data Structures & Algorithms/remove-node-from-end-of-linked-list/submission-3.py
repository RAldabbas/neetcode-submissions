# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1, ptr2 = head, head
        sz = 0
        i = 1
        
        while ptr1:
            ptr1 = ptr1.next
            sz += 1

        if n == 1 and sz == 1:
            return None
        elif sz == n:
            return head.next

        while i < sz - n:
            ptr2 = ptr2.next
            i += 1
        
        ptr2.next = ptr2.next.next
        
        return head

