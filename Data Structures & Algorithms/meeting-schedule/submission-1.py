"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # If intervals is empty
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)

        i = 0

        while True:
            if i == len(intervals)-1:
                break
            
            # Checking overlap with the next Interval
            if intervals[i].end > intervals[i+1].start:
                return False
            
            i += 1

        return True
