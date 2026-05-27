class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # len_n1 = len(nums1)
        # len_n2 = len(nums2)
        # arr = []
        # if len_n2 < len_n1:
        #     for elemn in nums2:
        #         if elemn in nums1 and elemn not in arr:
        #             arr.append(elemn)
        # else:
        #     for elemn in nums1:
        #         if elemn in nums2 and elemn not in arr:
        #             arr.append(elemn)
        # return arr
        n1 = set(nums1)
        n2 = set(nums2)
        return list(n1.intersection(n2))