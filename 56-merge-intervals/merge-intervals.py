class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #nlogn
        merged = []
        i = 1
        N = len(intervals)
        current = intervals[0]
        while i < N:
            
            if intervals[i][0] <= current[1]:
                current = [min(intervals[i][0], current[0]), max(intervals[i][1], current[1])]
            else:
                merged.append(current)
                current = intervals[i]
            
            i += 1
        
        merged.append(current)
        return merged
        