class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()

        def dfs(r, c, i):

            if i == len(word):
                return True

            if (
                r < 0 or c < 0 or
                r >= len(board) or
                c >= len(board[0]) or
                (r, c) in visited or
                word[i] != board[r][c]
            ):
                return False

            visited.add((r, c))
            nei = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]

            res = False
            for (a, b) in nei:
                temp = dfs(a, b, i + 1)
                res = res or temp

            visited.remove((r, c))

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False

            














        