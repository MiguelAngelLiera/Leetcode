class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for w in strs:
            while prefix != w[:len(prefix)]:
                prefix = prefix[:-1]
        return prefix