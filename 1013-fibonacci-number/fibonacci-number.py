class Solution:
    def fib(self, n: int) -> int:
        mem = [0, 1]
        if n == 0:
            return mem[0]
        for i in range(2, n + 1):
            mem.append(mem[i - 1] + mem[i - 2])
        return mem[-1]
        