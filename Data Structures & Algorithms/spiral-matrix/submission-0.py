class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = []

        top = 0
        l = 0
        r = COLS
        bottom = ROWS
        while l < r and top < bottom:
            # top row - every elem
            for j in range(l, r):
                res.append(matrix[top][j])
            top += 1

            # right col
            for i in range(top, bottom):
                res.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and top < bottom):
                break

            # bottom row
            for j in range(r - 1, l - 1, -1):
                res.append(matrix[bottom - 1][j])
            bottom -= 1

            # left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res

        # 1 2 3 6 9 8 7 4 5






