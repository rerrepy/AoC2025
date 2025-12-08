board = []
with open('day7.txt', 'r') as file:
    for line in file.readlines():
        board.append(list(line.strip()))
start_index = board[0].index('S')

rows = len(board)
cols = len(board[0])
score_board = [[0 for _ in range(cols)] for _ in range(rows)]
score_board[0][start_index] = 1

def is_not_oob(board, x, y):
    return 0 <= x < len(board[0]) and 0 <= y < len(board)

def check_splitter_under(board, x, y):
    if is_not_oob(board, x, y + 1):
        if board[y + 1][x] == '^':
            return True
    return False

def split_beam(board, x, y):
    if is_not_oob(board, x - 1, y + 1):
        board[y + 1][x - 1] = '|'
        score_board[y + 1][x - 1] += score_board[y][x]
    if is_not_oob(board, x + 1, y + 1):
        board[y + 1][x + 1] = '|'
        score_board[y + 1][x + 1] += score_board[y][x]
    return board

def move_beam_down(board, x, y):
    if is_not_oob(board, x, y + 1):
        board[y + 1][x] = '|'
        score_board[y + 1][x] += score_board[y][x]
    return board

def propagate_beam_one_step(board, x, y):
    score = 0
    if check_splitter_under(board, x, y):
        score += 1
        board = split_beam(board, x, y)
    else:
        board = move_beam_down(board, x, y)
    return board, score

score = 0
for y, line in enumerate(board):
    for x, ele in enumerate(line):
        if ele == '|' or ele == 'S':
            board, new_score = propagate_beam_one_step(board, x, y)
            score += new_score
score = 0
for i in score_board[-1]:
    score += i
    
print(score)
    