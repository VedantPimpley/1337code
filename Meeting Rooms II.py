"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        requires:
            len(intervals) >= 2

        algo:
            conflict occurs when end_i > start_j, where start_i <= start_j
            sort intervals by start times
            rooms_dict = {0: (intervals[0])}
            intervals = intervals[1:]
            for i in intervals:
                if i fits into any room, fit it in\
                i.e check conflict with most recent element only
                else create a new room, and put it in
            return number of rooms in room_dict
        '''

        # edge case
        n = len(intervals)
        if n == 0:
            return 0
        if n == 1:
            return 1

        # general case
        s_i = sorted(intervals, key=lambda e: e.start)
        rooms_map = {1: s_i[0].end}
        highest_room = 1
        s_i = s_i[1:]
        for i in s_i:
            scheduled = False
            for room in range(1,highest_room+1):
                rooms_latest_end_time = rooms_map[room]
                if rooms_latest_end_time > i.start:
                    #conflict
                    continue
                else:
                    if i.end > rooms_latest_end_time:
                        rooms_map[room] = i.end
                    scheduled = True
                    break
            if not scheduled:
                highest_room += 1
                rooms_map[highest_room] = i.end
        return highest_room