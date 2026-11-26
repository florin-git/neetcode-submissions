class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        
        def dfs(r, c, idx):

            if idx == len(word):
                return True

            if (
                r < 0 or c < 0 or
                r >= len(board) or
                c >= len(board[0]) or
                (r, c) in visited or
                board[r][c] != word[idx]
            ):
                return False

            visited.add((r, c))

            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            does_exist = False

            for (a, b) in nei:
                is_valid = dfs(a, b, idx + 1)
                does_exist = does_exist or is_valid

            visited.remove((r, c))

            return does_exist


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False









