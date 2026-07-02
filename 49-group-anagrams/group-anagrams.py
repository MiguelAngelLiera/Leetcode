from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        alpha = dict.fromkeys('abcdefghijklmnopqrstuvwxyz',0)
        for s in strs:
            ana = alpha.copy()
            for c in s:
                ana[c] += 1
            ana = tuple(ana.values())
            if ana in anagrams.keys():
                anagrams[ana].append(s)
            else:
                anagrams[ana] = [s]
        
        return list(anagrams.values())

        