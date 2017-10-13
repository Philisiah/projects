board = []


def create_board(run):
    for item in range(run):
        row = []
        for row_item in range(run):
            row.append(True)
        board.append(row)

# current row


def get_forward(i, j):
    return board[i][j + 1]


def get_back(x, y):
    return board[x][y - 1]
# upper row


def get_upper(g, h):
    return board[g - 1][h]


def get_upper_forward(k, l):
    return board[k - 1][l + 1]


def get_upper_back(m, n):
    return board[m - 1][n - 1]
# lowerrow


def get_lower(u, v):
    return board[u + 1][v]


def get_lower_back(t, s):
    return board[t + 1][s - 1]


def get_lower_forward(j, k):
    return board[j + 1][k + 1]

# Any live cell with fewer than two live neighbors dies


def first(p, n):
    truest = []
    if get_upper(p, n):
        truest.append(get_upper(p, n))
    if get_upper_back(p, n):
        truest.append(get_upper_back(p, n))
    if get_upper_forward(p, n):
        truest.append(get_upper_forward(p, n))
    if get_lower(p, n):
        truest.append(get_lower(p, n))
    if get_lower_back(p, n):
        truest.append(get_lower_back(p, n))
    if get_lower_forward(p, n):
        truest.append(get_lower_forward(p, n))
    if get_back(p, n):
        truest.append(get_back(p, n))
    if get_forward(p, n):
        truest.append(get_forward(p, n))
    if len(truest) < 2:
        return True
    return False

# Any live cell with more than three live neighbors dies


def second(pr, ni):
    truest = []
    if get_upper(pr, ni):
        truest.append(get_upper(pr, ni))
    if get_upper_back(pr, ni):
        truest.append(get_upper_back(pr, ni))
    if get_upper_forward(pr, ni):
        truest.append(get_upper_forward(pr, ni))
    if get_lower(pr, ni):
        truest.append(get_lower(pr, ni))
    if get_lower_back(pr, ni):
        truest.append(get_lower_back(pr, ni))
    if get_lower_forward(pr, ni):
        truest.append(get_lower_forward(pr, ni))
    if get_back(pr, ni):
        truest.append(get_back(pr, ni))
    if get_forward(pr, ni):
        truest.append(get_forward(pr, ni))
    if len(truest) >= 3:
        return True
    return False

# Any dead cell with exactly three live neighbors becomes a live cell


def third(tr, np):
    truest = []
    if get_upper(tr, np):
        truest.append(get_upper(tr, np))
    if get_upper_back(tr, np):
        truest.append(get_upper_back(tr, np))
    if get_upper_forward(tr, np):
        truest.append(get_upper_forward(tr, np))
    if get_lower(tr, np):
        truest.append(get_lower(tr, np))
    if get_lower_back(tr, np):
        truest.append(get_lower_back(tr, np))
    if get_lower_forward(tr, np):
        truest.append(get_lower_forward(tr, np))
    if get_back(tr, np):
        truest.append(get_back(tr, np))
    if get_forward(tr, np):
        truest.append(get_forward(tr, np))
    if len(truest) == 3:
        return True
    return False


# Transform Board
def transform():
    for row in range(len(board)):
        for col in range(len(board[row])):
            try:
                if board[row][col]:
                    if first(row, col):
                        board[row][col] = False
                        print(board)
                    if second(row, col):
                        board[row][col] = False
                        print(board)
                else:
                    if third(row, col):
                        board[row][col] == True
                        print(board)
                
            except IndexError:
                pass
            else:
                continue
create_board(3)
print(board)
# transform()
# print(board)
