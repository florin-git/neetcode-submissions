class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # x y z a z z

        # when duplicate -> update result
        # if duplicate -> move left until same char, and then move to next

        duplicates = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1

            duplicates.add(s[r])

            cur = r - l + 1
            res = max(res, cur)
            
        return res



