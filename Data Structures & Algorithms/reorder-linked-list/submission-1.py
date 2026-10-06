# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        prev = head

        # slow will be in middle of list
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        print(prev.val)
        prev.next = None

        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l1 = head
        l2 = prev
        prev = None

        while l1 and l2:
            nextL1 = l1.next
            nextL2 = l2.next
            l1.next = l2
            l2.next = nextL1
            prev = l2
            l1 = nextL1
            l2 = nextL2

        if l2:
            prev.next = l2
        



        
        