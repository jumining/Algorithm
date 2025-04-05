from collections import deque

# 입력
N = int(input())
K = int(input())

# 입력 - 사과 
apples = set()
for _ in range(K):
    y, x = map(int, input().split())
    apples.add((y-1, x-1))

# 입력 - 행동
L = int(input())
acts = {}
for _ in range(L):
    sec, dir = input().split()
    acts[int(sec)] = dir

snake = deque([(0,0)]) # 꼬리 제거하는 용도

def solution():
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 사전 뱀 시작 정보
    dir_idx = 0
    time = 0
    nhy, nhx = 0, 0

    while True:
        time += 1
        dy, dx = dir[dir_idx]
        nhy = nhy + dy
        nhx = nhx + dx

        # 몸 또는 벽 충돌
        if nhy < 0 or nhy >= N or nhx < 0 or nhx >= N or (nhy, nhx) in snake:
            return time

        # 한칸 움직이기
        snake.append((nhy, nhx))

        if (nhy, nhx) in apples:  # 사과 있음
            apples.remove((nhy, nhx))
        else:  # 사과 없음 → 꼬리 제거
            snake.popleft()

        if time in acts:
            if acts[time] == 'D':
                dir_idx = (dir_idx + 1) % 4
            elif acts[time] == 'L':
                dir_idx = (dir_idx - 1) % 4

print(solution())