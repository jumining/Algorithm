import sys
input = sys.stdin.readline

isUsed1 = [False]*40
isUsed2 = [False]*40
isUsed3 = [False]*40

cnt = 0

def func(cur):
    global cnt
    if cur==N:
        cnt += 1
        return
    for i in range(N):
        if isUsed1[i] or isUsed2[cur+i] or isUsed3[cur-i+N-1]:
            continue
        isUsed1[i] = True
        isUsed2[cur+i]=True
        isUsed3[cur-i+N-1]=True
        func(cur+1)
        isUsed1[i] = False
        isUsed2[cur+i]=False
        isUsed3[cur-i+N-1]=False

N = int(input())
func(0)
print(cnt)