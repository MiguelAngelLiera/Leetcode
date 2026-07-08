# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        N = 0
        while curr:
            N += 1
            curr = curr.next
        
        valid_iterations = N // k
        last = None
        prev = None
        curr = head

        for it in range(valid_iterations):
            fst = curr

            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if it == 0:
                head = prev

            if last:
                last.next = prev
            fst.next = curr
            last = fst
            prev = fst

            

        return head

            
        