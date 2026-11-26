class Solution:
    # time: O(n + v)
    # space: O(n + v)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        
        visited = set()
        def bfs(node):

            q = deque([node])

            while q:
                node = q.popleft()
                visited.add(node)

                for nei in graph[node]:
                    if nei not in visited:
                        q.append(nei)

        
        num_components = 0
        for i in range(n):
            if i not in visited:
                num_components += 1
                bfs(i)

        return num_components






