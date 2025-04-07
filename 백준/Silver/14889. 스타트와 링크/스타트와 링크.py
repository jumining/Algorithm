def combine(arr, r): # n개 중에 r개
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path[:])
            return
        
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i+1, path)
            path.pop()
    
    backtrack(0, [])
    return result

def calculate(arr):
    score = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            a, b = arr[i], arr[j]
            score += powers[a][b] + powers[b][a]
    return score

N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]
members = list(range(N))
minv = float('inf')

for a in combine(members, N//2):
    if 0 not in a:
        continue
    b = [x for x in members if x not in a]
    score_s = calculate(a)
    score_l = calculate(b)
    minv = min(minv, abs(score_s - score_l))

print(minv)