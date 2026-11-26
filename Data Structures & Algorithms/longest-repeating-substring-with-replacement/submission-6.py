class Solution:
    # time: O(26*n) = O(n)
    # space: O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_f = 0
        res = 0
        char_map = {}

        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)
            max_f = max(max_f, char_map[s[r]])

            while (r - l + 1) - max_f > k:
                char_map[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

