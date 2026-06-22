class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        mem = [0]
        for i, n in enumerate(nums):
            curr_sum = max(mem[-1] + n, n)
            mem.append(curr_sum)
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum
        
        