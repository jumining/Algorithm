from collections import deque
import sys
input = sys.stdin.readline

DIRS = [(-1,-1), (-1, 0),(-1,1), (1, 0),(1,-1), (0, -1), (0, 1),(1,1),(0,0)]

# 입력
walls = set()
maze = [list(input().strip()) for _ in range(8)]

# 함수
def move_walls():
    maze.pop()
    maze.insert(0, ['.']*8)

def in_range(y, x):
    return 0 <= y < 8 and 0 <= x < 8

def bfs():
    q = deque([(7,0)])

    while q:
        for _ in range(len(q)):
            y, x = q.popleft()

            if maze[y][x] == '#':
                continue

            if (y, x) == (0, 7):
                return 1

            for dy, dx in DIRS:
                ny, nx = y+dy, x+dx
                if in_range(ny, nx) and maze[ny][nx] == '.':
                    q.append((ny, nx))

        move_walls()

    return 0

# 구현
print(bfs())