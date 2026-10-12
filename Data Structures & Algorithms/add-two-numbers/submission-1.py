# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        temp = newHead
        carry = 0
        c1 = l1
        c2 = l2
        while c1 and c2:
            sum = c1.val + c2.val + carry
            if carry:
                carry = 0
            if sum > 9:
                carry = sum // 10
                sum = sum % 10
                

            temp.next = ListNode(sum)
            temp = temp.next
            if c1.next and not c2.next:
                c2.next = ListNode()
            elif c2.next and not c1.next:
                c1.next = ListNode()
            c1 = c1.next
            c2 = c2.next
        if carry:
            temp.next = ListNode(1)
        # while newHead:
        #     print(newHead.val)
        #     newHead = newHead.next
        return newHead.next
       