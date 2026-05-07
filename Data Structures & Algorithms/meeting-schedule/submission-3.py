"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # for interval in intervals:
        intervals.sort(key = lambda x : x.start)
        print(intervals)
        if intervals:
            end_start = intervals[0].end
            for inter in intervals[1:]:
                start , end = inter.start , inter.end
                if end_start > start:
                    return False
                end_start = end

        return True
        
