class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        min_height = n
        res = []
        for i in range(n):
            height = self.get_height(i, graph)

            if height == min_height:
                res.append(i)
            elif height < min_height:
                min_height = height
                res = [i]

        return res


    
    def get_height(self, root, graph):

        stack = [[root, -1, 0]]
        height = -1
        while stack:
            node, parent, h = stack.pop()
            height = max(height, h)

            for nei in graph[node]:
                if nei != parent:
                    stack.append([nei, node, h + 1])
        return height








