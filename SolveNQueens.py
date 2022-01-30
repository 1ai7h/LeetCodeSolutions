import numpy as np
def solveNQueens(n):
    col = set()
    pos_diag = set() #(r + c)
    neg_diag = set() #(r - c)

    result = []
    board = [["."] * n for i in range(n)]

    def solve(r):
        if r == n:
            copy_board = ["".join(row) for row in board]
            result.append(copy_board)
            return

        for c in range(n):
            if c in col or (r+c) in pos_diag or (r-c) in neg_diag:
                continue

            col.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)
            board[r][c] = 'Q'

            solve(r + 1)

            col.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
            board[r][c] = "."
    solve(0)
    print(np.matrix(result))


solveNQueens(5)
