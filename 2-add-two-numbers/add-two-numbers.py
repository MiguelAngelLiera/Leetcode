# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode() 
        head = l3
        carry = 0
        while l1 or l2:
            a = 0 if not l1 else l1.val
            b = 0 if not l2 else l2.val
            c =  a+b + carry 
            carry = c // 10
            l3.val = c % 10

            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next
            
            if carry or l1 or l2:
                l3.next = ListNode()
                l3 = l3.next
        if carry:
            l3.val = carry

        return head
            
            
        