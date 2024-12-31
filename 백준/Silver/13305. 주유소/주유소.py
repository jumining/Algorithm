n_city = int(input())
l_roads = list(map(int, input().split()))
c_liters = list(map(int, input().split()))

result = 0
for idx, cost in enumerate(c_liters):
    if idx < n_city-1 and cost == min(c_liters[idx:-1]):
        result += cost * sum(l_roads[idx:])
        break
    else:
        result += cost * l_roads[idx]

print(result)