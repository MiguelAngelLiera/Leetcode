class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1, 1]
        for i in range(2, n + 1):
            mem.append(mem[i - 1] + mem[i - 2])
        
        return mem[-1]
        