import heapq as hq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frecs = dict.fromkeys(set([str(i) for i in nums]),0)
        for n in nums:
            frecs[str(n)] += 1
        
        frecs = [(v, k_) for k_, v in frecs.items()]
        h = []
        
        for f in frecs:
            hq.heappush(h, f)
            if len(h) > k:
                hq.heappop(h)

        top_k = [int(v) for f, v in h]

        return top_k