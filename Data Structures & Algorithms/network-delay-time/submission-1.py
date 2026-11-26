class Solution:
    # Dijkstra's Algorithm (For shortest path)
    # time: O(e log v)
    # space: O(v + e)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # dist = {i: float("inf") for i in range(1, n + 1)}
        # dist[k] = 0

        graph = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            graph[u].append([v, t])

        min_heap = [(0, k)]
        visited = set()

        res = -1
        while min_heap:
            t, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            res = max(res, t)
            visited.add(u)

            for nei, w in graph[u]:
                if nei not in visited:
                    heapq.heappush(min_heap, (t + w, nei))

        return res if len(visited) == n else -1




