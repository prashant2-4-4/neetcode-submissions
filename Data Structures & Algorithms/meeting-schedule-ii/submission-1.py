"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # when processing request check which room is free.

        room_free = []
        intervals.sort(key = lambda x : x.start)
        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            flag = True
            for end_time in range(len(room_free)):
                if start >= room_free[end_time]:
                    room_free[end_time] = end
                    flag = False
                    break
            
            if flag:
                room_free.append(end)
                

        return len(room_free)




        