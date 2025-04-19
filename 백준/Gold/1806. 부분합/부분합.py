import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

st = en = sum = 0
ans = float("inf")

while True:
    if sum >= S:
        ans = min(ans, en-st)
        sum -= nums[st]
        st += 1

    elif sum < S:
        if en == N:
            break
        sum += nums[en]
        en += 1

print(ans) if ans!=float("inf") else print(0)