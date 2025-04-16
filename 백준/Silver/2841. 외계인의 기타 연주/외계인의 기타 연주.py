import sys
input = sys.stdin.readline

N, P = map(int, input().split())
guitar = [[] for _ in range(7)]

cnt = 0
for _ in range(N):
    line, fret = map(int, input().split())

    while guitar[line] and guitar[line][-1] > fret:
        guitar[line].pop()
        cnt += 1

    if not guitar[line] or guitar[line][-1] < fret:
        guitar[line].append(fret)
        cnt += 1

print(cnt)