import sys
input = sys.stdin.readline

dic = []
for _ in range(int(input())):
    dic.append((tuple(map(int, input().split()))))
dic = sorted(dic, key=lambda x : (x[1], x[0]))    

ans = []
cnt = 0
cur_st, cur_en = 0, 0
for st, en in dic:
    if st == en:
        cur_en = en
        cnt += 1
        ans.append((st,en))
        continue
    if st >= cur_en:
        cur_st, cur_en = st, en
        cnt += 1
        ans.append((st,en))
print(len(ans))