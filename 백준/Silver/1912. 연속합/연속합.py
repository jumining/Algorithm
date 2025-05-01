n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
cur_sum = arr[0]

for i in range(1, n):
    cur_sum = max(cur_sum+arr[i], arr[i]) # 이전부터 수열을 이어갈지 or 자기부터 다시 시작할지
    max_sum = max(max_sum, cur_sum)

print(max_sum)