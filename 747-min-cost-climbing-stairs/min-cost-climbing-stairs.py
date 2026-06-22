class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        cost.append(0)
        mem = cost[0: 2]
        for i in cost[2: N + 1]:
            mem.append(i + min(mem[-1], mem[-2]))
        
        return mem[-1]
        