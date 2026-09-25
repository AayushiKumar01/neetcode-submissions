"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)

        rooms = []

        for interval in intervals:

            # If the earliest available room is free,
            # reuse it
            if rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)

            # Add this meeting's ending time
            heapq.heappush(rooms, interval.end)

        return len(rooms)

        