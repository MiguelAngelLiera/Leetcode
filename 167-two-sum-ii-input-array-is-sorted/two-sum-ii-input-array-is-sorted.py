class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum_ = numbers[left] + numbers[right]
        while sum_ != target and left < right:
            if sum_ > target:
                right -= 1
            if sum_ < target:
                left += 1
            sum_ = numbers[left] + numbers[right]
        
        return [left + 1, right + 1]
        