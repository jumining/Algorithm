import sys
sys.stdin = open("testcase.txt", "r")

from collections import deque

# 입력
N,M,K = map(int, input().split())
towers = {}
board = [[0]*M for _ in range(N)]
cnt = 0
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        alive = True
        if arr[j] == 0:
            board[i][j] = 1
            alive = False
        cnt += 1
        towers[cnt] = {
            'pos' : (i, j),
            'power' : arr[j],
            'time': 0,
            'alive': alive
        }

# 함수
def select_attacker(towers, time):
    alive_towers = [(num, tower) for (num, tower) in towers.items() if tower['alive']]
    alive_towers.sort(key=lambda tower: (
        tower[1]['power'],
        -tower[1]['time'],
        -(tower[1]['pos'][0] + tower[1]['pos'][1]),
        -tower[1]['pos'][1]
    ))
    attacker_id, attacker_info = alive_towers[0]
    attacker_info['time'] = time
    attacker_info['power'] += N+M
    return attacker_id, attacker_info

def select_target(towers, time):
    alive_towers = [(num, tower) for (num, tower) in towers.items() if tower['alive'] and tower['pos'] != (ay, ax)]
    alive_towers.sort(key=lambda tower: (
        -tower[1]['power'],
        tower[1]['time'],
        (tower[1]['pos'][0] + tower[1]['pos'][1]),
        tower[1]['pos'][1]
    ))

    target_id = alive_towers[0][0]
    target_info = alive_towers[0][1]
    return target_id, target_info

def bfs(sy,sx,ty,tx):
    q = deque()
    q.append((sy,sx,[]))
    visited = [[0]*M for _ in range(N)]
    visited[sy][sx] = 0
    while q:
        y, x, path = q.popleft()
        if (y,x) == (ty, tx):
            return path[:-1], True
        for dy, dx in ((0,1),(1,0),(0,-1),(-1,0)):
            ny, nx = (y+dy)%N, (x+dx)%M
            if not visited[ny][nx] and not board[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, path + [(ny,nx)]))
    return [], False

# 구현
for time in range(1,K+1):

    if time > 1 and all(not tower['alive'] for tower in towers.values() if tower['pos'] != (ay, ax)):
        break  # 조기 종료

    # [1] 공격자 선정
    attacker_id, attacker_info = select_attacker(towers, time)
    ay, ax = attacker_info['pos']

    if all(not tower['alive'] for tower in towers.values() if tower['pos'] != (ay, ax)):
        break  # 조기 종료

    # [2] 공격자 공격
    target_id, target_info = select_target(towers, time) # 공격 대상 찾기
    ty, tx = target_info['pos']

    turrets_attack = False
    path, has_way = bfs(ay, ax, ty, tx)

    cur_power = towers[attacker_id]['power']
    towers[target_id]['power'] -= cur_power
    if has_way:    # 레이저 공격
        for y, x in path:
            cur_id = (y * M) + (x + 1)
            towers[cur_id]['power'] -= cur_power // 2

    if not has_way: # 안되면 포탑 공격
        group = []
        for dy, dx in ((0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)):
            ny, nx = (ty+dy)%N, (tx+dx)%M
            if (ny,nx) != (ay, ax) and not board[ny][nx]:
                cur_id = (ny * M) + (nx + 1)
                group.append(cur_id)
                towers[cur_id]['power'] -= cur_power // 2

    # [3] 포탑 부서짐
    for tower in towers.values():
        if tower['power'] <= 0:
            tower['alive'] = False
            tower['power'] = 0
            board[tower['pos'][0]][tower['pos'][1]] = 1

    # [4] 포탑 정비
    not_irrelevant = []
    not_irrelevant.append(attacker_id)
    not_irrelevant.append(target_id)
    if has_way:
        path_id = [M*py+(px+1) for py, px in path]
        not_irrelevant += path_id
    if not has_way:
        not_irrelevant += group

    for id in range(1, N*M+1):
        if id not in not_irrelevant and towers[id]['alive']:
            towers[id]['power'] += 1

    power_board =[[0] * M for _ in range(N)]

    for _, info in towers.items():
        y, x = info['pos']
        power_board[y][x] = info['power']

max_power = max(tower['power'] for tower in towers.values())
print(max_power)
