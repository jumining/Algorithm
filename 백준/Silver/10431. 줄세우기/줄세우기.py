testCase = int(input())
for _ in range(testCase):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(0, 20):
        for j in range(1, 20-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    print(arr[0], cnt)
