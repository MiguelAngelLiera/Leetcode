import heapq as hq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        heap = []
        if nums1:
            heap.append((nums1[0], 1))
            nums1 = nums1[1:]
        if nums2:
            heap.append((nums2[0], 2))
            nums2 = nums2[1:]
        hq.heapify(heap)
        nums3 = []
        while heap:
            elem, original_array = hq.heappop(heap)
            nums3.append(elem)
            if original_array == 1 and nums1:
                hq.heappush(heap, (nums1[0], 1))
                nums1 = nums1[1:]
            elif original_array == 2 and nums2:
                hq.heappush(heap, (nums2[0], 2))
                nums2 = nums2[1:]
        
        n_3 = len(nums3)
        if not n_3:
            return []
        if n_3 % 2 == 1:
            return nums3[n_3//2]
        else:
            return (nums3[n_3//2] + nums3[(n_3//2) - 1])/2

        