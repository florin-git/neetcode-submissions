class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start with two pointers l, r from 0
        # use a hash_map to store (chars, pos) in current substring
        # if a new letter was already appearing the substring, then
        # shift left to that position + 1 and update curre substring

        chars_map = {}
        l, r = 0, 0
        res = 0
        # a b b a

        while r < len(s):
            if s[r] in chars_map:
                last_pos = chars_map[s[r]]
                l = max(last_pos + 1, l)

            chars_map[s[r]] = r
            res = max(res, r - l + 1)
            print(r, res)
            r += 1
            
        return res













