class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        char_map = {}

        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)

            while (r - l + 1) - max(char_map.values()) > k:
                char_map[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

