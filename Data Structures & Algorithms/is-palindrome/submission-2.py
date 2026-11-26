class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.is_alphanumeric(s[l]):
                l += 1
            while r > l and not self.is_alphanumeric(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


    def is_alphanumeric(self, s: str) -> bool:

        for c in s:
            if not c.isalpha() and c not in list(map(str, range(0, 10))):
                return False

        return True 