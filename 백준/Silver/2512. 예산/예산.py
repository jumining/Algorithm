import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

if sum(budgets) <= M:
    print(max(budgets))
else:
    l, r = 0, max(budgets)
    result = 0
    while l <= r:
        mid = (l + r) // 2
        total = sum(min(budget, mid) for budget in budgets)

        if total <= M:
            result = mid
            l = mid + 1
        else:
            r = mid - 1

    print(result)
