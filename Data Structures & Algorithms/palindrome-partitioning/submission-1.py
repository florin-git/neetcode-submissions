class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def dfs(l, r, cur):

            if r >= len(s):
                if l == r:
                    res.append(cur.copy())
                return

            
            if self.is_palindrome(s[l: r + 1]):
                cur.append(s[l: r + 1])
                dfs(r + 1, r + 1, cur)
                cur.pop()

            dfs(l, r + 1, cur)

        dfs(0, 0, [])
        return res

        
    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True