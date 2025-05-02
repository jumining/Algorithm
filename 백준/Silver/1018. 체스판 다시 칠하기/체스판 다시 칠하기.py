import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_repaint(x, y, first_color, other_color):
    count = 0
    for i in range(8):
        for j in range(8):
            expected = first_color if (i+j) % 2 == 0 else other_color
            if board[x + i][y + j] != expected:
                count += 1
    return count

min_val = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        repaint_w = count_repaint(i, j, 'W', 'B')  # 왼쪽 위가 W일 때
        repaint_b = count_repaint(i, j, 'B', 'W')  # 왼쪽 위가 B일 때
        current_min = min(repaint_w, repaint_b)
        min_val = min(min_val, current_min)
print(min_val)