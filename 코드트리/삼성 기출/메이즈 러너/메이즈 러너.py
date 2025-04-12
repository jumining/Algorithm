# 메이즈러너

# 함수 - 최소 정사각형 구하기 -> (좌상단 y좌표, 좌상단 x좌표, 변의 길이)
def get_rectangle():
    global ey, ex
    for l in range(2, N+1): # 한 변의 길이
        for y in range(0, N-l+1):
            for x in range(0, N-l+1):
                for py, px in players:
                    if y<=py<y+l and x<=px<x+l and y<=ey<y+l and x<=ex<x+l:
                        return y, x, l

# 함수 - 시계 방향 90도 회전, 내구도 감소 -> (90도 회전하고 내구도 깎인 2차원 배열)
def rotate(arr, ry, rx, rlen):
    global ey, ex

    # 시계 방향 90도 회전
    rotated_arr = [list(reversed(row)) for row in zip(*arr)]

    # 출구 위치 업데이트
    ey, ex = ex-rx+ry, rlen-1-ey+ry+rx

    # 플레이어 위치 업데이트
    new_players = []
    for y, x in players:
        if ry<=y<=ry+rlen-1 and rx<=x<=rx+rlen-1:
            ny, nx = x-rx+ry, rlen-1-y+ry+rx
            new_players.append((ny,nx))
            continue
        new_players.append((y,x))

    # 내구도 깎기
    for row in rotated_arr:
        for x in range(len(row)):
            if row[x] > 0:
                row[x] -=1

    return rotated_arr, new_players

# 함수 - 배열을 미로에 적용하기
def merge_arr_to_board(ry, rx, rlen, rotated_arr):
    # 해당하는 모든 좌표를 돌면서 바뀔 배열 내용을 미로에 적용하기
    for y in range(rlen):
        for x in range(rlen):
            board[y+ry][x+rx] = rotated_arr[y][x]

# 함수 - 모든 참가자 이동
def move_all_players():
    global total_distance

    moved_players = []
    for py, px in players:
        # 최단 방향으로 이동
        if ey < py and board[py-1][px] == 0: # 위
            total_distance += 1
            moved_players.append((py-1, px))
        elif ey > py and board[py+1][px] == 0:
            total_distance += 1
            moved_players.append((py+1, px))
        elif ex > px and board[py][px+1] == 0:
            total_distance += 1
            moved_players.append((py, px+1))
        elif ex < px and board[py][px-1] == 0:
            total_distance += 1
            moved_players.append((py, px-1))
        else:
            moved_players.append((py, px))

        # 출구면 제거
        moved_players = [(py, px) for py, px in moved_players if (py, px) != (ey, ex)]

    return moved_players

# 입력
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
players = [tuple(int(x)-1 for x in input().split()) for _ in range(M)]
ey, ex = map(lambda x: int(x) - 1, input().split())

# 구현
total_distance = 0
for _ in range(K):
    # 모든 참가자 한칸씩 이동
    players = move_all_players()

    # 조기 종료
    if len(players) == 0:
        break

    # 미로 회전
    ry, rx, rlen = get_rectangle()
    rectangle_arr = [row[rx:rx+rlen] for row in board[ry:ry+rlen]]
    rotated_rectangle_arr, players = rotate(rectangle_arr, ry, rx, rlen)
    merge_arr_to_board(ry, rx, rlen, rotated_rectangle_arr)

# 출력
print(total_distance)
print(ey+1, ex+1)
