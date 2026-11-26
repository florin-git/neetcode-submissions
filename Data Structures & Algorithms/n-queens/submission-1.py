class Solution:
    # time: O(n!)
    # space: O(n^2)
    def solveNQueens(self, n: int) -> List[List[str]]:

        # place a queen in a position
        # add this position to a set
        # for each position in the grid, try to place a new queen
        # if the new queen can't be placed return, otherwise place it

        # if I placed 4 queen then add the resulting board to the result

        res = []
        placed_columns = set()
        diffs = set()
        sums = set()

        board = [["." for _ in range(n)] for _ in range(n)]

        def dfs(r):

            if r == n:
                b = ["".join(row) for row in board]
                res.append(b)
                return


            for c in range(n):
                if (
                    c in placed_columns or
                    r - c in diffs or
                    r + c in sums
                ):
                    continue

                placed_columns.add(c)
                diffs.add(r - c)
                sums.add(r + c)
                board[r][c] = "Q"
                
                dfs(r + 1)

                placed_columns.remove(c)
                diffs.remove(r - c)
                sums.remove(r + c)
                board[r][c] = "."

        dfs(0)
        return res








        