class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : (x[0] , x[1]))
        
        new_intervals = []
        n = len(intervals)
        interval_range = intervals[0]
        for i in range(1 , n):
            if intervals[i][0] <= interval_range[1]:
                interval_range[1] = max(intervals[i][1] , interval_range[1])
            else:
                new_intervals.append(interval_range)
                interval_range = intervals[i]

        new_intervals.append(interval_range)
    
        return new_intervals

        