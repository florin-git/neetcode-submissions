class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for w in words for c in w}
        in_degree = {k: 0 for k in graph.keys()}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""     

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        q = deque()
        for k, v in in_degree.items():
            if v == 0:
                q.append(k)

        res = []

        while q:
            n = q.popleft()
            res.append(n)

            for ne in graph[n]:
                in_degree[ne] -= 1
                if in_degree[ne] == 0:
                    q.append(ne)

        if len(res) != len(in_degree):
            return ""

        return "".join(res)




