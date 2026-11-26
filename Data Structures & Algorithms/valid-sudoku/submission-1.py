class Solution:
    # # time: O(1) constant because the sudoku has fixed size of 9x9
    # # space: O(1)
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
        
    #     n = len(board)


    #     for r in range(n):
    #         seen = set()
    #         for c in range(n):
    #             if board[r][c] == ".":
    #                 continue

    #             if board[r][c] in seen:
    #                 return False

    #             seen.add(board[r][c])


    #     for c in range(n):
    #         seen = set()
    #         for r in range(n):
    #             if board[r][c] == ".":
    #                 continue

    #             if board[r][c] in seen:
    #                 return False

    #             seen.add(board[r][c])



    #     for square in range(n):
    #         seen = set()
    #         for i in range(n // 3):
    #             for j in range(n // 3):
    #                 r = (square // 3) * 3 + i
    #                 c = (square % 3) * 3 + j

    #                 if board[r][c] == ".":
    #                     continue

    #                 if board[r][c] in seen:
    #                     return False

    #                 seen.add(board[r][c])

    #     return True

    # time: O(1) constant because the sudoku has fixed size of 9x9
    # space: O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


