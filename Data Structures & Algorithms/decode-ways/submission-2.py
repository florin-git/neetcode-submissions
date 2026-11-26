class Solution:
    # time: O(n)
    # space: O(n)
    def numDecodings(self, s: str) -> int:

        cache = [1 for _ in range(len(s) + 1)]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                cache[i] = 0
            else:
                cache[i] = cache[i + 1]

            if i < len(s) - 1 and (s[i] == '1' or
                   (s[i] == '2' and s[i + 1] < '7')):
                cache[i] += cache[i + 2]

        return cache[0]