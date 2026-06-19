class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums1)
        pos_nums1 = {}

        for k, n in enumerate(nums1):
            pos_nums1[n] = k
        
        for e in nums2:
            while len(stack) > 0 and stack[-1] < e:
                last = stack.pop()
                idx = pos_nums1.get(last, None)
                if idx is not None:
                    res[idx] = e
            stack.append(e)

        return res


        