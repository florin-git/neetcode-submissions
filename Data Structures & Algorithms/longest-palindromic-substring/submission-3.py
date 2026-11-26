class Solution:
    # time: O(n^2)
    # space: O(n) for the output but actually it doesn't need extra space
    def longestPalindrome(self, s: str) -> str:
        
        start = 0
        res = 0 

        for i in range(len(s)):
            
            # odd case
            l, r = i, i
            start, res = self.check_palindrom(s, l, r, start, res)

            # even case
            l, r = i, i + 1
            start, res = self.check_palindrom(s, l, r, start, res)

        return s[start: start + res]


    def check_palindrom(self, s: str, l: int, r: int, start: int, res: int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res:
                res = r - l + 1
                start = l
            l -= 1
            r += 1

        return start, res





