class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[b] += 1
            graph[a].append(b)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        num_visited = 0
        while q:
            n = q.popleft()
            num_visited += 1

            for nei in graph[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return num_visited == numCourses











