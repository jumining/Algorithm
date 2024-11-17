N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
idx = [arr[i][0] for i in range(N)].index(K)
for i in range(N):
    if arr[idx][1:] == arr[i][1:]:
        print(i + 1)
        break
