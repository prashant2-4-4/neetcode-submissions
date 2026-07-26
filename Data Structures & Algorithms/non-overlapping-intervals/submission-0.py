class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0] , x[1]))
        print(intervals)
        removal = 0
        n = len(intervals)
        interval_range = intervals[0][:]
        for i in range(1 , n):
            if intervals[i][0] < interval_range[1]:
                interval_range[1] = min(intervals[i][1] , interval_range[1])
                removal += 1
            else:
 
                interval_range = intervals[i][:]


    
        return removal
        