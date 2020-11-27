def nQueen(board, N):
    # Base case: if queen have been placed , return True
    if N == 0:
        return True
    # Place the first queen
    for i in range(len(board)):
        for j in range(len(board)):

            # check if cell is a good cell
            if isbadCell(board, i, j):
                continue
            board[i][j] = 1

            # Check if the remaining N-1 queens be placed successfuly
            if nQueen(board, N-1):
                # If yes return True: we are done
                return True

            # if not undo the previous placement and try other cells
            board[i][j] = 0
    # if no good cell is available and N != 0
    return False


def isbadCell(board, x, y):
    row, col = len(board), len(board[0])
    # check if any cell in the xth row of board
    for i in range(row):
        if board[x][i] == 1:
            return True

    # check if any cell in the yth columns of board
    for j in range(col):
        if board[j][y] == 1:
            return True

    # check for cell (p,q) along the diagonal of cell(x,y)
    for i in range(row):
        for j in range(col):
            if (i + j) == (x+y) and board[i][j] == 1:
                return True
            elif (i-j) == (x-y) and board[i][j] == 1:
                return True
    return False


if __name__ == "__main__":
    N = int(input())
    board = [[0 for i in range(N)] for _ in range(N)]
    ret = nQueen(board, N)
    if ret:
        print('YES')
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=' ')
                if j == len(board)-1:
                    print()
        print('NO')
