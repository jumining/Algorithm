import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int,input().split()))

l, r = max(arr), sum(arr)

def get_cnt():
    cnt = 1
    tmp = 0
    for a in arr:
        if tmp+a > m:
            cnt += 1
            tmp = a
        else:
            tmp += a
    return cnt

while l<=r:
    m = (r+l)//2
    cnt = get_cnt()
    # print(f"# {l}, {m}, {r} : {cnt}")

    if cnt > M:
        l = m+1
    else: 
        r = m-1

print(l)