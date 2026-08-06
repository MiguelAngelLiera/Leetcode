class Solution:
    """
    [34,23,1,24,75,33,54,8]
    [26, 37, 59, -1, 27, 6, 52]
    [[23,1,24,75,33,54,8], .,[33,54,8], [8, 54], [inf, 8], [inf, -inf]] = [nums[i-1]] + [aux[i-1]]
    
    
    target = 60
    
    60 - 34 = 26 
    
    sum = 0
    34 
    
    
    """
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        sum_ = -1
        
        for i in range(N-1, -1, -1):
            target = k - nums[i]
            for j in nums[i+1:]:
                if target > j:
                    sum_ = max(sum_, nums[i] + j)
                
        return sum_
        
        