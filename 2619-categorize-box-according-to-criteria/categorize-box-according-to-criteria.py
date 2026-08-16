class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        v = length * width * height
        cond1 = (length >= 10**4 or width >= 10**4 or height >= 10**4 or mass >= 10**4) or v >= 10**9
        cond2 = mass >= 100
        if cond1 and cond2:
            return "Both"
        if not cond1 and not cond2:
            return "Neither"
        if cond1 and not cond2:
            return "Bulky"
        if not cond1 and cond2:
            return "Heavy"