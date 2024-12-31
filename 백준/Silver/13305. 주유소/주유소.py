n_city = int(input())
l_roads = list(map(int, input().split()))
c_liters = list(map(int, input().split()))

result = 0
min_cost = c_liters[0]

for idx in range(n_city - 1):
    min_cost = min(min_cost, c_liters[idx])
    result += min_cost * l_roads[idx]

print(result)