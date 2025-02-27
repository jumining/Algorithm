from itertools import combinations

import sys
input = sys.stdin.readline

for i in combinations([int(input()) for _ in range(9)], 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        
        break