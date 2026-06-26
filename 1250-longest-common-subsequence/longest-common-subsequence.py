class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        mem = [[0]*(M+1) for i in range(N+1)]

        for i in range(1, N+1):
            for j in range(1, M+1):
                if text1[i-1] == text2[j-1]:
                    mem[i][j] = mem[i-1][j-1] + 1
                else:
                    mem[i][j] = max(mem[i][j-1], mem[i-1][j])

        return mem[-1][-1]
        