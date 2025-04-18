import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
yarr = [0]
xarr = [0]
for _ in range(K):
    a, b = map(int, input().split())
    if a==0:
        yarr.append(b)
    else:
        xarr.append(b)
yarr.sort()
yarr.append(M)
xarr.sort()
xarr.append(N)

ygap = []
xgap = []
for i in range(len(yarr)-1):
    ygap.append(yarr[i+1]-yarr[i])
for i in range(len(xarr)-1):
    xgap.append(xarr[i+1]-xarr[i])
print(max(ygap) * max(xgap))