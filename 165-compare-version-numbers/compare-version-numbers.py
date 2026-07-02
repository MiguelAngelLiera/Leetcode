class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 += "."
        version2 += "."
        i = 0
        j = 0
        while version1 or version2:
            num1 = 0
            num2 = 0
            if version1:
                while version1[i] != ".":
                    i += 1
                num1 = int(version1[:i])
                version1 = version1[i+1:]
                i = 0
            if version2:
                while version2[j] != ".":
                    j += 1
                num2 = int(version2[:j])
                version2 = version2[j+1:]
                j = 0
            if num1 > num2:
                return 1
            if num2 > num1:
                return -1
        return 0
        