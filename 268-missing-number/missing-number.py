class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        remain = list(range(0, n+1))
        for n in nums:
            remain[n] = 0
        return sum(remain)