class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s1)
        M = len(s2)
        if M + N != len(s3):
            return False
        mem = [[0] * (M + 1) for i in range(N +1)]

        mem[0][0] = 1 

        for i in range(1, N+1):
            if s1[i-1] == s3[i-1] and mem[i-1][0]:
                mem[i][0] = 1
        for j in range(1, M+1):
            if s2[j-1] == s3[j-1] and mem[0][j-1]:
                mem[0][j] = 1
        
        for i in range(1, N+1):
            for j in range(1, M+1):
                if mem[i-1][j] == 1 and s3[i+j-1] == s1[i-1]:
                    mem[i][ j] = 1
                if mem[i][j-1] == 1 and s3[i+j-1] == s2[j-1]:
                    mem[i][j] = 1

        
        return bool(mem[-1][-1])
                
        