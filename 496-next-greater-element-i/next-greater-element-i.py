class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1]*len(nums1)
        s_nums1 = set(nums1)
        for i, e in enumerate(nums2):
            while len(stack) > 0 and stack[-1] < e:
                last = stack.pop()
                if last in s_nums1:
                    idx = nums1.index(last)
                    res[idx] = e
            stack.append(e)

        return res


        