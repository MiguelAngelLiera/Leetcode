from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        letters = {'a', 'b', 'c'}
        N = len(s)
        j = 3
        count = 0
        c = {'a': 0, 'b': 0, 'c':0}
        for e in s[0: 3]:
            c[e] = 1
        
        for i in range(N - 3 + 1):
            while sum(list(c.values())) < 3 and j < N:
                j += 1
                c[s[j-1:j]] = 1
            if sum(list(c.values())) == 3:
                count += 1 + (N - j)
                if j - (i + 1) < 3:
                    j += 1
            c[s[i:i+1]] = 1 if s[i] in s[i+1:j] else 0
            #c.subtract(s[i:i+1])
        return count
            







    # def numberOfSubstrings(self, s: str) -> int:
    #     letters = {"a", "b", "c"}
    #     N = len(s)
    #     count = 0
    #     for window_size in range(3, N + 1):
    #         for i in range(0, N+1 -window_size):
    #             if set(s[i: i + window_size]) == letters:
    #                 count += 1

    #     return count


        