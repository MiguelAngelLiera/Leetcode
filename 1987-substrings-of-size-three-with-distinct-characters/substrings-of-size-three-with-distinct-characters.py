class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        j = i + 3
        N = len(s)
        goods = 0
        while i <= N - 3:
            if len(set(s[i:j])) == 3:
                goods += 1
            i += 1
            j += 1
        return goods

            


        