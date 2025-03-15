from collections import deque
import sys

input = sys.stdin.readline

d = ((-2,-1),(-1,-2),(2,-1),(1,-2),(-2,1),(-1,2),(2,1),(1,2))

def is_valid(y, x):
    return 0<=y<N and 0<=x<N

def bfs(y, x):
    visit = [[False] * N for _ in range(N)]
    q = deque([(y, x, 0)])
    visit[y][x] = True
    while q:
        y, x, depth = q.popleft()
        if y==d1 and x==d2:
            return depth
        for dy, dx in d:
            n_y, n_x = y+dy, x+dx
            if is_valid(n_y, n_x) and not visit[n_y][n_x]:
                q.append((n_y, n_x, depth+1))
                visit[n_y][n_x] = True

for _ in range(int(input())):
    N = int(input())
    a, b = map(int, input().strip().split())
    d1, d2 = map(int, input().strip().split())
    print(bfs(a,b))