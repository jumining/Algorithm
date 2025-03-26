import sys
input = sys.stdin.readline

isUsed1 = [False]*30
isUsed2 = [False]*30
isUsed3 = [False]*30

N = int(input())
cnt = 0

def func(cur):
    global cnt
    if cur==N:
        cnt += 1
        return
    for i in range(N):
        if isUsed1[cur+i] or isUsed2[cur-i+N-1] or isUsed3[i]:
            continue
        isUsed1[cur+i] = True
        isUsed2[cur-i+N-1] = True
        isUsed3[i] = True
        func(cur+1)
        isUsed1[cur+i] = False
        isUsed2[cur-i+N-1] = False
        isUsed3[i] = False

func(0)
print(cnt)