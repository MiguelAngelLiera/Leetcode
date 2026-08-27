from collections import defaultdict
class Solution:
    """
    [5,3,4,1]
    [2] : [[], [5]], |  [[1], [ 4]]
    []
    """
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        res = 0
        left_l = dict.fromkeys(range(N), 0)
        left_m = dict.fromkeys(range(N), 0)
        right_l = dict.fromkeys(range(N), 0)
        right_m = dict.fromkeys(range(N), 0)
        for i in range(N):
            #print(f"i: {i}")
            for j in range(i):
                if rating[i] > rating[j]:
                    left_l[i] += 1
                else:
                    left_m[i]+= 1
                    
            for j in range(i+1, N):
                if rating[i] > rating[j]:
                    right_l[i]+= 1
                else:
                    right_m[i]+= 1
               
        res = 0
        for i in range(N):
            res += left_l[i] * right_m[i]
            res += left_m[i] * right_l[i]
            
        return res
    
    """
    
    def numTeams(self, rating: List[int]) -> int:
        a = self.aux_numTeams(rating)
        b = self.aux_numTeams(rating[::-1])
        return a+b
        
    def aux_numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        res = 0
        for i in range(N):
            for j in range(i+1,N):
                if rating[i] < rating[j]:
                    for k in range(j+1, N):
                        if rating[j] < rating[k]:
                            res += 1
        return res
    """
            
        