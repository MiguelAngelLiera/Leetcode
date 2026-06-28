class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        mem = [[1, 1] for _ in  range(N)]


        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if mem[j][0] + 1 == mem[i][0]:
                        mem[i][1] += mem[j][1] 
                        
                    elif mem[j][0] + 1 > mem[i][0]:
                        mem[i][1] = mem[j][1]
                        mem[i][0] = mem[j][0] + 1



        max_lenght = 0
        
        for m, c in mem:
            if m > max_lenght:
                max_lenght = m
        
        n_lis = 0
        for m, c in mem:
            if m == max_lenght:
                n_lis += c

        return n_lis

        