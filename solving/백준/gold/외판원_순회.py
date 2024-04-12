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
    # 모든 도시를 방문했을 경우
    if visited == (1 << n) - 1:
        # 현재 도시에서 출발 도시로 가는 간선이 있는지 확인
        if world[cur][0]:
            return world[cur][0]
        else:
            return INF

    # 이미 최소 비용이 계산되었다면 바로 리턴
    if (cur, visited) in dp:
        return dp[(cur, visited)]

    # 현재 도시와 방문 집합에 대한 최소 비용 구하기
    min_cost = INF
    for next in range(1, n):
        # next 도시로 가는 간선이 없거나 이미 next에 방문했는지 확인
        if world[cur][next] == 0 or visited & (1 << next) != 0:
            continue
        updated_visited = visited | (1 << next)  # next 도시를 visited에 추가
        # 재귀 사용해서 부분 문제의 해 계산
        min_cost = min(min_cost, world[cur][next] + dfs(next, updated_visited))
    dp[(cur, visited)] = min_cost
    return min_cost


print(dfs(0, 1))
