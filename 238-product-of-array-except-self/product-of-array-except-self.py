class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prod = 1
        o_prod = 1
        answer = [0]*N
        n_zeros = 0
        for n in nums:
            if n == 0:
                n_zeros += 1
            else:
                o_prod *= n
            prod *= n
            
            
        for i in range(N):
            if nums[i] != 0:
                answer[i] = int(prod/nums[i])
            elif n_zeros == 1 :
                answer[i] = o_prod
            else:
                answer[i] = 0


        return answer

        