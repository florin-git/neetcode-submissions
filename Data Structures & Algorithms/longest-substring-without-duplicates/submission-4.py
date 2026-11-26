class Solution:
    # time: O(n)
    # space: O(m), m=number of unique chars in s
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in duplicates:
                l = max(duplicates[s[r]] + 1, l)

            duplicates[s[r]] = r
            cur = r - l + 1
            res = max(res, cur)
            
        return res



