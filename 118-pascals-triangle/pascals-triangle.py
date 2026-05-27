class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        old_rows = self.generate(numRows-1)
        old_level = old_rows[-1]
        n = len(old_level)
        i = 0
        new_level = [1]
        while i < n - 1:
            new_level.append(old_level[i] + old_level[i+1])
            i += 1
        new_level.append(1)

        old_rows.append(new_level)

        return old_rows

             
        