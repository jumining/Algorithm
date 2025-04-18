import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

yarr = [0, M]
xarr = [0, N]

for _ in range(K):
    a, b = map(int, input().split())
    if a==0:
        yarr.append(b)
    else:
        xarr.append(b)

yarr.sort()
xarr.sort()

max_y_gap = max(yarr[i+1] - yarr[i] for i in range(len(yarr)-1))
max_x_gap = max(xarr[i+1] - xarr[i] for i in range(len(xarr)-1))

print(max_y_gap * max_x_gap)
