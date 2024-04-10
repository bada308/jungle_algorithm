'''
https://www.acmicpc.net/problem/2098
외판원 순회
'''

import sys
input = sys.stdin.readline
INF = int(1e8)

n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]
dp = {}


def dfs(cur, visited):
    if visited == (1 << n) - 1:
        if world[cur][0]:
            return world[cur][0]
        else:
            return INF

    if (cur, visited) in dp:
        return dp[(cur, visited)]

    min_cost = INF
    for next in range(1, n):
        if world[cur][next] == 0 or visited & (1 << next) != 0:
            continue
        updated_visited = visited | (1 << next)
        min_cost = min(min_cost, world[cur][next] + dfs(next, updated_visited))
    dp[(cur, visited)] = min_cost
    return min_cost


print(dfs(0, 1))
