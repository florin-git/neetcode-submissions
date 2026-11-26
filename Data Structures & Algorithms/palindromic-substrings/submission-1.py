class Solution:
    # time: O(n**2)
    # space: O(1)
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            # odd
            res += self.count_palindrome(s, i, i)
            # even
            res += self.count_palindrome(s, i, i + 1)
            
        return res

    def count_palindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

            