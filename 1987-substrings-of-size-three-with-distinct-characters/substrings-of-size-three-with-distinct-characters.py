class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        j = i + 3
        N = len(s)
        goods = 0
        while i <= N - 3:
            sub = s[i:j]
            if len(set(sub)) == 3:
                goods += 1
            i += 1
            j += 1

        return goods

            


        