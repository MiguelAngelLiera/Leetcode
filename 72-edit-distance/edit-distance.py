class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        # INF = float('inf')
        mem = [[0]*(M+1) for i in range(N + 1)]
        # mem[0][0] = 0
        for j in range(M+1):
            mem[0][j] = j
        for i in range(N+1):
            mem[i][0] = i

        for i in range(1, N+1):
            for j in range(1, M + 1):
                if  word1[i - 1] == word2[j-1]:
                    mem[i][j] = mem[i-1][j-1]
                if word1[i - 1] != word2[j-1]:
                    mem[i][j] = min(mem[i-1][j-1], mem[i][j-1], mem[i-1][j]) + 1

        res = mem[-1][-1]
        # if res == float('inf'):
        #     return M ^ N

        return res

        