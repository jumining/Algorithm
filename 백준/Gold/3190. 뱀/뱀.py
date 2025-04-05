from collections import deque

# 방향 정보 변환
def rotate(dy, dx, cmd):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx = directions.index((dy, dx))
    if cmd == 'D':  # 오른쪽 회전
        idx = (idx + 1) % 4
    elif cmd == 'L':  # 왼쪽 회전
        idx = (idx - 1) % 4
    
    # print(f"[방향 전환] '{cmd}' 입력 → 새로운 방향: {directions[idx]}")
    return directions[idx]

# 디버깅용 출력 함수
def printArr(title, arr):
    print(f"--- {title} ---")
    for row in arr:
        print(*row)
    print()

N = int(input())
K = int(input())
snake = [[0] * N for _ in range(N)]

# 사과 위치정보 배열 입력
apples = [[0] * N for _ in range(N)]
for _ in range(K):
    y, x = map(int, input().split())
    apples[y-1][x-1] = 1

# 행동 정보 배열에 저장
L = int(input())
acts = []
for _ in range(L):
    sec, dir = map(str, input().split())
    acts.append((int(sec), dir))

def solution():
    # 사전 뱀 시작 정보
    hy, hx = 0, 0
    dy, dx = 0, 1
    snake[hy][hx] = 1
    cnt = 0
    length = 1
    q = deque()
    q.append((hy, hx))

    acts.append((10001, ''))

    for sec, next_dir in acts:
        while True:
            if cnt == sec:
                dy, dx = rotate(dy, dx, next_dir)
                # print(f"[{cnt}초] 방향 전환 완료 → 다음 이동\n")
                break    
            cnt += 1
            hy += dy
            hx += dx

            # print(f"[{cnt}초] 뱀 머리 이동: ({hy}, {hx})")

            # 벽에 부딪힘
            if hy < 0 or hy >= N or hx < 0 or hx >= N:
                # print("💥 벽에 충돌!")
                return cnt
            
            # 자기 몸에 부딪힘
            if snake[hy][hx] == 1:
                # print("💥 자기 몸에 충돌!")
                return cnt

            # 한칸 움직이기
            snake[hy][hx] = 1
            q.append((hy, hx))

            if apples[hy][hx] == 1:  # 사과 있음
                apples[hy][hx] = 0
                length += 1
                # print("🍎 사과 먹음! 길이 증가")
            else:  # 사과 없음 → 꼬리 제거
                ty, tx = q.popleft()
                snake[ty][tx] = 0
                # print(f"🐍 꼬리 제거 at ({ty}, {tx})")

            # printArr(f"시간 {cnt} 뱀 상태", snake)

        

# 프린트
# printArr('초기 사과 위치', apples)
print(solution())