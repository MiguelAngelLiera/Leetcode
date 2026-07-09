# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        res = None
        head_res = None
        for i, l in enumerate(lists):
            if l:
                hq.heappush(heap, (l.val, i))
                lists[i] = l.next
        while heap:
            n_element, o_list = hq.heappop(heap)
            if res:
                res.next=ListNode(n_element)
                res = res.next
            else:
                res = ListNode(n_element)
                head_res = res
            #res.nex
            if not lists[o_list] is None:
                hq.heappush(heap, (lists[o_list].val, o_list))
                lists[o_list] = lists[o_list].next
            

        return head_res


        