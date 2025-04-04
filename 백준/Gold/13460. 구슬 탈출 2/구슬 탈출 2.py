from collections import deque

graph = []
dydx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dydx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# 배열 입력, 구슬 위치 저장
N, M = map(int, input().split())
for i in range(N):
    graph.append(list(input()))
    for j in range(M):
        if graph[i][j] == 'R':
            ry, rx = i, j
        elif graph[i][j] == 'B':
            by, bx = i, j

# 구슬 이동
def move(y, x, dy, dx):
    while graph[y+dy][x+dx] != '#' and graph[y][x] != 'O':
        y += dy
        x += dx
    return y, x

def dir_name(dy, dx):
    directions = {
        (-1, 0): '위',
        (1, 0): '아래',
        (0, -1): '왼쪽',
        (0, 1): '오른쪽'
    }
    return directions.get((dy, dx), '알 수 없는 방향')

# bfs 진행
def bfs():
    global rx, ry, bx, by
    visited = []
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited.append((rx, ry, bx, by))
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        # print(f"[BFS 단계] cnt: {cnt}, 빨간 구슬 위치: ({ry}, {rx}), 파란 구슬 위치: ({by}, {bx})")
        
        if cnt > 10:
            return -1
        for dy, dx in dydx:
            nry, nrx = move(ry, rx, dy, dx)
            nby, nbx = move(by, bx, dy, dx)

            # 파란 구슬이 구멍에 도착
            if graph[nby][nbx] == 'O':
                continue

            # 빨간 구슬이 구멍에 도착
            if graph[nry][nrx] == 'O':
                return cnt

            # 같은 위치에 도착 -> 늦게 도착한 구슬 뒤로 한칸 이동
            if (nby, nbx) == (nry, nrx):

                rd = abs(nrx - rx) + abs(nry - ry)
                bd = abs(nbx - bx) + abs(nby - by)
                if rd > bd:
                    nrx -= dx
                    nry -= dy
                else:
                    nby -= dy
                    nbx -= dx

            # print(f"→ 방향: {dir_name(dy, dx)}")
            # print(f"   빨간 구슬 이동: ({ry}, {rx}) → ({nry}, {nrx})")
            # print(f"   파란 구슬 이동: ({by}, {bx}) → ({nby}, {nbx})")
        
            # 예전에 방문 안했으면 큐에 추가, cnt++
            if (nrx, nry, nbx, nby) not in visited:
                # print("   ✅ 새로운 상태 - 큐에 추가")
                q.append((nrx, nry, nbx, nby, cnt+1))
                visited.append((nrx, nry, nbx, nby))

    return -1

print(bfs())