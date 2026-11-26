class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        q = deque()
        for i, d in enumerate(indegree):
            if d == 0:
                q.append(i)

        while q:
            i = q.popleft()

            for nei in graph[i]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

            graph[i] = []

        for i in range(numCourses):
            if graph[i] != []:
                return False

        return True


