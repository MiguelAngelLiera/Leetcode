"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        new_head = None
        new_curr = None
        corresp = {}
        randoms = {}

        while curr:
            if not new_head:
                new_head = Node(curr.val)
                new_curr = new_head
                
            else:
                new_curr.next = Node(curr.val)
                new_curr = new_curr.next
            
            corresp[curr] = new_curr
            randoms[curr] = curr.random
            curr = curr.next

        curr = head
        new_curr = new_head
        while curr:
            tmp_rnd = randoms[curr]
            new_curr.random = None if not tmp_rnd else corresp[tmp_rnd]
            curr = curr.next
            new_curr = new_curr.next

        return new_head
            

        
        