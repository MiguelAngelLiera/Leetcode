class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = str(n)
        s = 0
        power = len(digits)
        for d in digits:
            s += int(d)**power
            
        return s == n
        