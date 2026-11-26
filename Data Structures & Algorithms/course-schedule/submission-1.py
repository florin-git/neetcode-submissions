class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # check if there are cycles in the graph. If yes return False, True otherwise


        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        # write a dfs function that start at a node
        # loop over all nodes and call dfs

        visited = set()
        for n in range(numCourses):            
            if n not in visited:
                is_cycle = self.dfs(n, graph, visited)
                if is_cycle:
                    return False

        return True

    
    def dfs(self, node, graph, visited):
        if not graph[node]:
            return False

        if node in visited:
            return True
        
        visited.add(node)

        for nei in graph[node]:
            if self.dfs(nei, graph, visited):
                return True

        visited.remove(node)
        graph[node] = []

        return False










