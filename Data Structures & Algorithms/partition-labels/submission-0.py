class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # a b b e r  a
        # x y x

        indices = defaultdict(int)
        for i, c in enumerate(s):
            indices[c] = i

        l = 0
        res = []
        max_i = 0

        for r in range(len(s)):
            max_i = max(max_i, indices[s[r]])

            if max_i == r:
                res.append(r - l + 1)
                l = r + 1

        return res
