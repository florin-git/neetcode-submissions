class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > (n - 1):
            return False

        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return True

            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue

                if dfs(nei, node):
                    return True

            return False

        # if there are cycles and disconnected components, then it's not a tree
        if dfs(0, -1) or len(visited) != n:
            return False

        return True
            




