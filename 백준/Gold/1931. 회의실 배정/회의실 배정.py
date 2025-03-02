import sys
input = sys.stdin.readline

dic = []
for _ in range(int(input())):
    dic.append((tuple(map(int, input().split()))))

dic = sorted(dic, key=lambda x : (x[1], x[0]))    
cnt = 0
t = 0
for st, en in dic:
    if st >= t:
        t = en
        cnt += 1
print(cnt)