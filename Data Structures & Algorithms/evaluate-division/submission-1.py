class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(node, trg, cur, visited):
            if node == trg:
                return cur
            
            visited.add(node)

            for nei, val in graph[node]:
                if nei not in visited: 
                    res = dfs(nei, trg, cur * val, visited)
                    if res != -1.0:
                        return res

            return -1
        
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]

            graph[a].append((b, v))
            graph[b].append((a, 1/v))

        res = []
        for src, trg in queries:
            if src not in graph or trg not in graph:
                res.append(-1.0)
                continue
            
            op = dfs(src, trg, 1.0, set())
            res.append(op)

        return res
            

        








