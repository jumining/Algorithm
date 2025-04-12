# import sys
# sys.stdin = open("testcase.txt", "r")

from collections import deque
dirs = [(-1,0),(0,-1),(0,1),(1,0)]

# 함수
def in_range(y, x):
    return 0<=y<n and 0<=x<n

def get_first_step_toward_store(people):
    q = deque()
    v = [[False]*n for _ in range(n)]
    y, x = people['pos']
    q.append((y, x, []))
    v[y][x] = True

    while q:
        yy, xx, path = q.popleft()
        if (yy,xx) == people['store']:
            return path[0]
        for dy, dx in dirs:
            ny, nx = yy + dy, xx + dx
            if in_range(ny,nx) and not v[ny][nx] and walls[ny][nx] == 0:
                q.append((ny, nx, path + [(ny, nx)]))
                v[ny][nx] = True


def select_baseyx_from_storeyx(sy, sx):
    q = deque()
    v = [[False]*n for _ in range(n)]

    q.append((sy, sx, 0))
    v[sy][sx] = True
    candidates = []

    while q:
        y, x, d = q.popleft()
        if (y,x) in basecamp:
            candidates.append((d, y, x))
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if in_range(ny,nx) and not v[ny][nx] and walls[ny][nx] == 0:
                q.append((ny, nx, d+1))
                v[ny][nx] = True

    candidates.sort()
    return candidates[0][1], candidates[0][2]

# 입력
n, m = map(int, input().split())
basecamp = set()
for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(n):
        if tmp[x] == 1:
            basecamp.add((y,x))
walls = [[0] * n for _ in range(n)]
peoples = {}
for i in range(1, m+1):
    a, b = map(int, input().split())
    peoples[i] = {
        'pos': (-1,-1),
        'store': (a-1, b-1),
        'arrived' : False,
    }

# 구현
time = 0
while True:
    time += 1
    # print(f"⏰ {time}분")
    if all(p['arrived'] for p in peoples.values()):
        break

    # 1. 이동
    for p in peoples.values():
        if p['pos'] != (-1,-1) and not p['arrived']:
            ny, nx = get_first_step_toward_store(p)
            p['pos'] = (ny, nx)

    # 2. 도착 확인
    for p in peoples.values():
        if p['pos'] == p['store']:
            p['arrived'] = True
            ny, nx = p['pos']
            walls[ny][nx] = 1

    # 3. 베이스 캠프 선택
    if time <= m:
        sy, sx = peoples[time]['store']
        by, bx = select_baseyx_from_storeyx(sy, sx)
        peoples[time]['pos'] = (by, bx)
        walls[by][bx] = 1

# 출력 - 모든 사람이 편의점에 도착하는 시간
print(time-1)
