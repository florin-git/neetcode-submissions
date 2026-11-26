class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()

        def dfs(r, c, cur):

            if cur == word:
                return True

            if (
                r < 0 or c < 0 or
                r >= len(board) or
                c >= len(board[0]) or
                (r, c) in visited or
                len(cur) > len(word)
            ):
                return False

            visited.add((r, c))
            nei = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]

            res = False
            cur += board[r][c]
            for (a, b) in nei:
                temp = dfs(a, b, cur)
                res = res or temp

            cur = cur[:-1]
            visited.remove((r, c))

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, ""):
                    return True

        return False

            














        