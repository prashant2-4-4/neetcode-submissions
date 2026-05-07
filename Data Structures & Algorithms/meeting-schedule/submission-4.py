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
        # print(intervals)
        # if intervals:
        # end_start = intervals[0].end
        for i in range(1, len(intervals)):
            # start , end = inter.start , inter.end
            if intervals[i].start < intervals[i-1].end:
                return False

        return True
        
