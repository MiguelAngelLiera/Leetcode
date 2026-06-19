class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = set()
        N = len(nums)
        nums.sort() #onlogn
        visited_k = set()
        for k, e in enumerate(nums[:-2]):
            if e in visited_k:
                continue
            target = -e
            left = k + 1
            right = N - 1

            while left < right:
                sum_ = nums[left] + nums[right]
                if sum_ == target:
                    triplet = (e, nums[left], nums[right])
                    if triplet not in triplets:
                        triplets.add(triplet)
                    right -= 1
                    left += 1
                elif sum_ > target:
                    right -= 1
                elif sum_ < target:
                    left += 1
            
            visited_k.add(e)
                
                
        return list(triplets)

            

        