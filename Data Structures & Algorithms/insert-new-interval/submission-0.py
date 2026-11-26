class Solution:
    # time: O(n)
    # space: O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        l, r = 0, len(intervals) - 1
        new_start = newInterval[0]

        while l <= r:
            m = (l + r) // 2

            s, _ = intervals[m]

            if new_start > s:
                l = m + 1
            else:
                r = m - 1

        intervals.insert(l, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
