class Solution:
    # time: O(n), since we just have 26 elements
    # space: O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # compute frequency
        freq = {}
        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)

        # max heap to pick the max in O(1)
        max_heap = []
        for t, f in freq.items():
            heapq.heappush(max_heap, -f)

        time = 0
        q = deque() # pairs of [-f, idleTime]

        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                f = 1 + heapq.heappop(max_heap) # increment since negative

                if f:
                    q.append([f, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time




        