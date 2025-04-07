def calculate(total, num, op):
    if op == 0:
        return total + num
    elif op == 1:
        return total - num
    elif op == 2:
        return total * num
    elif op == 3:
        return int(total / num) if total * num >= 0 else -(-total // num)

def dfs(total, idx, operators):
    global maxv, minv
    if idx == N:
        maxv = max(maxv, total)
        minv = min(minv, total)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            next_total = calculate(total, nums[idx], i)
            dfs(next_total, idx + 1, operators)
            operators[i] += 1

# 입력
N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split())) # +, - , *, //

# 초기값
maxv = -float('inf')
minv = float('inf')

# dfs 실행
dfs(nums[0], 1, operators)

# 출력
print(maxv)
print(minv)