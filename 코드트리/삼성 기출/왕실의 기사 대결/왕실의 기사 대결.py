# 디버깅에 많은 시간 소요

from collections import deque

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
kor = ["위", "우", "아래", "좌"]

# util 함수
def get_area(knight, dy, dx):
    r, c = knight['pos']
    h, w = knight['size']
    return [(r+y+dy, c+x+dx) for x in range(w) for y in range(h)]

def get_group(first, d):
    visited = set()
    q = deque()
    q.append(first)
    visited.add(first)
    dy, dx = DIRS[d]
    while q:
        cur = q.popleft()
        area1 = set(get_area(knights[cur], dy, dx))
        for other in range(1, N+1):
            if other == cur or not knights[other]['alive']: continue
            area2 = set(get_area(knights[other],0,0))
            if area1 & area2 and other not in visited:
                q.append(other)
                visited.add(other)
    return list(visited)

# 동작 함수
def can_move(group, d):
    dy, dx = DIRS[d]
    for k in group:
        knight = knights[k]
        for y,x in get_area(knight,0,0):
            ny, nx = y+dy, x+dx
            if not (0<=ny<L and 0<=nx<L):
                # print(f"  ❌ 범위 밖으로 나감, {k}번 기사, {ny, nx}")
                return False
            if board[ny][nx] == 2: # 벽
                # print(f"  ❌ 벽 만남, {k}번 기사, {ny, nx}")
                return False
    return True

def move_group(group, d, first):
    global total_damage
    dy, dx = DIRS[d]
    for k in group: # 이동
        knight = knights[k]
        r, c = knight['pos']
        knight['pos'] = (r+dy, c+dx)
    for k in group: # 데미지
        knight = knights[k]
        if k == first: continue
        if not knight['alive']: continue
        for y, x in get_area(knight,0,0):
            if board[y][x] == 1: # 함정
                knight['hp'] -= 1
                knight['damage'] += 1
                if knight['hp'] == 0:
                    knight['alive'] = False
                    break
                # print(f"damage: {k}번 기사 {y,x}에서 함정")

# 입력
L, N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]
knights = {}
for i in range(1,N+1):
    r,c,h,w,k = map(int, input().split())
    knights[i] = {
        'pos' : (r-1, c-1),
        'size': (h,w),
        'hp' : k,
        'alive' : True,
        'damage' : 0
    }
cmds = [tuple(map(int, input().split())) for _ in range(Q)]

# 수행
total_damage = 0
cnt = 0
for i, d in cmds:
    cnt+=1
    # print(f"\n# {cnt} {i}번 기사 {kor[d]}로 한 칸 이동, {total_damage}")
    if not knights[i]['alive']:
        continue
    group = get_group(i, d)
    if can_move(group, d):
        move_group(group, d, i)
    # for k, v in knights.items():
        # print(f"{k}번 기사 {v['pos']}, h,w:{v['size']}")

print(sum(knights[k]['damage'] for k in knights if knights[k]['alive']))
