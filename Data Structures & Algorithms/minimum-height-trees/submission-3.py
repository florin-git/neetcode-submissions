class Solution:
    # time: O(v + e)
    # space: O(v)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        edge_cnt = {}
        leaves = deque()

        for src, nei in enumerate(graph):
            if len(nei) == 1:
                leaves.append(src)
            edge_cnt[src] = len(nei)

        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1

                for nei in graph[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

        return list(leaves)





