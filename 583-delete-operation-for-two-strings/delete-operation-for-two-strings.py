class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        mem = [[0] * (M+1) for _ in range(N+1)]

        mem[0] = list(range(0, M + 1))
        for r in range(0, N+1):
            mem[r][0] = r

       
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if word1[i-1] == word2[ j-1]:
                    mem[i][j] = mem[i-1][j-1]
                else:
                    mem[i][j] = min( mem[i-1][j], mem[i][j - 1]) + 1

        return mem[-1][-1]