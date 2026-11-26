class Solution:
    def validPalindrome(self, s: str) -> bool:
        

        res = self.check_palindrome(s)
        for i in range(len(s)):
            res = res or self.check_palindrome(s[:i] + s[i+1:])
        return res

    def check_palindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
