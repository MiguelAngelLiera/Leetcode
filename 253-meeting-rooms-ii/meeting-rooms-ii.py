import heapq as hq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = 1
        N = len(intervals)
        meeting_rooms=1
        endings = [intervals[0][1]]
        while i < N:
            if endings and endings[0] <= intervals[i][0]:
                hq.heappop(endings)
                
            else:
                meeting_rooms += 1

            hq.heappush(endings, intervals[i][1])
            
            
            i += 1
        return meeting_rooms
        