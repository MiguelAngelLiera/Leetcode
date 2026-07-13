class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        for i in range(N):
            nums[i] = (nums[i], i)
        nums = self.unrotate_array(nums)
        return self.binary_search(nums, target)
        

    def unrotate_array(self, nums: List[int]) -> List[int]:
        N = len(nums)
        pivot = self.find_pivot(nums, 0, N-1)
        nums = nums[pivot:] + nums[:pivot]
        return nums
    
    def find_pivot(self, nums: List[int], i, j) -> List[int]:
        N = j + 1 - i
        if N == 1:
            return i
        mid = i + N // 2
        if nums[i][0] <= nums[mid][0] <= nums[j][0]:
            return i
        if nums[mid][0] < nums[i][0]:
            return self.find_pivot(nums, i+1, mid)

        if nums[mid][0] > nums[j][0]:
            return self.find_pivot(nums, mid+1, j)

    def binary_search(self, nums: List[int], target) -> int:
        N = len(nums)
        if N == 0: 
            return -1
        if N == 1:
            return nums[0][1] if nums[0][0] == target else -1
        mid = N // 2
        if nums[mid][0] < target:
            return self.binary_search(nums[mid+1:], target)
        if nums[mid][0] > target:
            return self.binary_search(nums[:mid], target)
        return nums[mid][1]


        

        