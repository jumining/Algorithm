import sys
input = sys.stdin.readline

def dfs(pos, total):
    global max_power

    if pos == 11:
        max_power = max(max_power, total)
        return

    for i in range(11):
        if not is_used[i] and powers[pos][i]:
            is_used[i] = True
            dfs(pos + 1, total + powers[pos][i])
            is_used[i] = False

T = int(input())
for _ in range(T):
    powers = [list(map(int, input().split())) for _ in range(11)]

    max_power = 0
    is_used = [False] * 11

    dfs(0, 0)
    print(max_power)