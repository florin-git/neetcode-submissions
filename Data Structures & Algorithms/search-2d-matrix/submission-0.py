class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # the column number in the matrix version can be found
        # as i % column_number

        # the row is i // column_numer

        ROWS = len(matrix)
        COLS = len(matrix[0])

        full_length = ROWS * COLS
        l, r = 0, full_length - 1

        while l <= r:
            m = l + (r - l) // 2
            row = m // COLS
            col = m % COLS

            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1

        return False
            








        