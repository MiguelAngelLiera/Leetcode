from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, l in enumerate(s):
            if c[l] == 1:
                return i

        return -1


        