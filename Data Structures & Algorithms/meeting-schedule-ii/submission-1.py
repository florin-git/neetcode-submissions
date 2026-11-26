"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # time: O(nlog n)
    # space: O(n)
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # if there is a conflict that we need another room

        # maximum overlapping intervals at any point
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s, e = 0, 0
        res = 0
        count = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                res = max(res, count)
                s += 1
            else:
                count -= 1
                e += 1

        # if I exist and I still need to iterate over ends it's okay to return
        # since count can't increase

        return res
                










