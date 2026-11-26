class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [[] for _ in range(n)]

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        
        num_components = 0
        for i in range(n):
            if i not in visited:
                num_components += 1
                dfs(i)

        return num_components






