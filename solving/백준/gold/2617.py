'''
https://www.acmicpc.net/problem/2617
구슬 찾기
'''

import sys
input = sys.stdin.readline
INF = int(1e8)

n, m = map(int, input().split())
table = [[INF]*n for _ in range(n)]

# 본인 -> 본인 비용 0으로 초기화
for i in range(n):
    table[i][i] = 0

# 간선 입력 받기, 비용 1으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    table[a-1][b-1] = 1


# 플로이드 워샬 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            if table[i][j] > table[i][k] + table[k][j]:
                table[i][j] = table[i][k] + table[k][j]

# 진입 & 진출 차수
indegree = [0 for _ in range(n)]
outdegree = [0 for _ in range(n)]

# 진입 & 진출 차수 카운트
for i in range(n):
    for j in range(n):
        if table[i][j] != INF and table[i][j] != 0:
            indegree[j] += 1
            outdegree[i] += 1

answer = 0

# 진입 & 진출 차수가 중간값보다 크면 중간이 될 수 없음
for idg in indegree:
    if idg > n // 2:
        answer += 1

for odg in outdegree:
    if odg > n // 2:
        answer += 1

print(answer)