# 1h 소요 

def move(dir, new_board):
    result = []
    if dir == 0: # up
        for col in zip(*(new_board)):
            non_zero = [x for x in col if x != 0]
            result.append(non_zero + [0] * (N-len(non_zero)))
        result = list(map(list, zip(*result)))

    elif dir == 1: # right
        for i in range(N):
            non_zero = [x for x in new_board[i] if x != 0]
            result.append([0] * (N-len(non_zero)) + non_zero)

    elif dir == 2: # down
        for col in zip(*(new_board)):
            non_zero = [x for x in col if x != 0]
            result.append([0] * (N-len(non_zero)) + non_zero)
        result = list(map(list, zip(*result)))

    elif dir == 3: # left
        for i in range(N):
            non_zero = [x for x in new_board[i] if x != 0]
            result.append(non_zero + [0] * (N-len(non_zero)))
    return result

def merge(dir, new_board):
    new_board = [row[:] for row in new_board]
    if dir == 0: # up
        for col in range(N):
            for y in range(N-1):
                if new_board[y][col] != 0 and new_board[y][col] == new_board[y+1][col]:
                    new_board[y][col] = new_board[y][col] * 2
                    new_board[y+1][col] = 0

    elif dir == 1: # right
        for row in range(N):
            for x in range(N-1, 0, -1):
                if new_board[row][x] != 0 and new_board[row][x] == new_board[row][x-1]:
                    new_board[row][x] = new_board[row][x] * 2
                    new_board[row][x-1] = 0

    elif dir == 2: # down
        for col in range(N):
            for y in range(N-1, 0, -1):
                if new_board[y][col] != 0 and new_board[y][col] == new_board[y-1][col]:
                    new_board[y][col] = new_board[y][col] * 2
                    new_board[y-1][col] = 0

    elif dir == 3: # left 
        for row in range(N):
            for x in range(N-1):
                if new_board[row][x] != 0 and new_board[row][x] == new_board[row][x+1]:
                    new_board[row][x] = new_board[row][x] * 2
                    new_board[row][x+1] = 0
    return new_board

def dfs(depth, board):
    global max_num

    if depth == 5:
        max_num = max(max_num, max(max(row) for row in board))
        return
    
    for dir in range(4):
        new_board = [row[:] for row in board]
        new_board = move(dir, new_board)
        new_board = merge(dir, new_board)
        new_board = move(dir, new_board)

        if new_board != board:
            dfs(depth+1, new_board)

# 입력 
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

# 시뮬레이션
max_num = max(max(row) for row in board)
dfs(0,board)
print(max_num)