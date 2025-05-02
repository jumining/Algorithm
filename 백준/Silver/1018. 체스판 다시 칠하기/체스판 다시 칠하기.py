import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_repaint(x, y):
    count = 0
    for i in range(8):
        for j in range(8):
            expected = 'W' if (i+j) % 2 == 0 else 'B'
            if board[x + i][y + j] != expected:
                count += 1
    return count

min_val = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        repaint_w = count_repaint(i, j)
        current_min = min(repaint_w, 64 - repaint_w)
        min_val = min(min_val, current_min)
print(min_val)