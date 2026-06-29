class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        z = self._reverse(s)
        N = len(s)
        mem = [[0] * (N + 1) for _ in range(N + 1)]

        for i in range(1, N+1):
            for j in range(1, N+1):
                if s[i-1] == z[j-1]:
                    mem[i][j] = mem[i-1][j-1] + 1
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j-1])

        return mem[-1][-1]
    

    def _reverse(self, s: str) -> str:
        z = ""
        for i in range(len(s)-1, -1, -1):
            z += s[i]
        return z