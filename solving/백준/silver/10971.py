# https://www.acmicpc.net/problem/10971

import sys
import math
from itertools import permutations
input = sys.stdin.readline

n = int(input())

cost_table = [list(map(int, input().split())) for _ in range(n)]
route_list = list(permutations(list(range(1, n)), n - 1))

answer = math.inf

for route in route_list:
    isTraversable = True
    route = [0] + list(route) + [0]
    total = 0
    for i in range(len(route) - 1):
        if(cost_table[route[i]][route[i+1]] == 0):
            isTraversable = False
            break
        total += cost_table[route[i]][route[i+1]]
    if total < answer and isTraversable:
        answer = total

print(answer)