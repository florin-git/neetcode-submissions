class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def dfs(i, r, c):

            if i == len(word):
                return True


                
            if (
                r < 0 or c < 0 or
                r > len(board) - 1 or
                c > len(board[0]) - 1 or
                (r, c) in visited or
                board[r][c] != word[i]
            ):
                return False

            

            visited.add((r, c))

            nei = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            res = False
            for a, b in nei:
                res = res or dfs(i + 1, a, b)

            visited.remove((r, c))

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0, r, c):
                    return True

        return False


