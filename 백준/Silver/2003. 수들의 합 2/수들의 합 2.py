import sys
input = sys.stdin.readline

n, target = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
c = 0
total = 0

while True:
    if total >= target:
        total -= arr[l]
        l += 1
    elif r == n:
        break
    elif total < target:
        total += arr[r]
        r += 1

    if total == target:
        c += 1

print(c)