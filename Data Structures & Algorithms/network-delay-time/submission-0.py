class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dist = [float("inf") for _ in range(n)]
        dist[k - 1] = 0

        graph = [[] for _ in range(n)]

        for u, v, t in times:
            graph[u - 1].append([v - 1, t])

        q = deque([[k - 1, 0]])

        while q:
            n, t = q.popleft()

            for nei, w in graph[n]:
                if t + w < dist[nei]:
                    dist[nei] = t + w
                    q.append([nei, t + w])

        res = max(dist)

        return res if res < float("inf") else -1
