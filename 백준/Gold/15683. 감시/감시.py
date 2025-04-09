# 10:30-11:50 (1h 20m 소요)

# 감시 영역 칠하는 함수
def fill(y,x,dirs,board):
    modified = []
    for d in dirs:
        ny, nx = y, x
        dy, dx = FDIR[d]
        while True:
            ny += dy
            nx += dx

            # 범위 벗어남
            if not (0<=ny<N and 0<=nx<M): 
                break

            # 벽 만남
            if board[ny][nx] == 6:
                break

            # CCTV 만남
            if board[ny][nx] == 0:
                board[ny][nx] = 7 # str 성능 손해 
                modified.append((ny,nx))       
    return modified

# board 원상복구 - deep copy보다 성능 향상
def undo(board, modified):
    for y, x in modified:
        board[y][x] = 0
    
# dfs
def dfs(depth, board):
    global min_blind
    if depth == len(cctv):
        cur_blind = sum(row.count(0) for row in board) 
        min_blind = min(min_blind, cur_blind)
        return
    
    y, x, type = cctv[depth]
    for dirs in DIR[type]:
        modified = fill(y,x,dirs,board)
        dfs(depth+1, board)
        undo(board, modified)

# 입력
N, M = map(int, input().split())
board = []
cctv = []
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(M):
        if 0 < row[x] < 6:
            cctv.append((y, x, row[x]))
    board.append(row)

# 시뮬레이션    
min_blind = float('inf')
FDIR = [(-1,0),(0,1),(1,0),(0,-1)]
DIR = {
    1: [(0,),(1,),(2,),(3,)],
    2: [(0,2), (1,3)],
    3: [(0,1),(1,2),(2,3),(3,0)],
    4: [(0,1,2), (1,2,3), (2,3,0), (3,0,1)],
    5: [(0,1,2,3)]
}
dfs(0, board)
print(min_blind)