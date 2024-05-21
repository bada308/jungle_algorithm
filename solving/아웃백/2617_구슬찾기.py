'''
https://www.acmicpc.net/problem/2617
'''
import sys
input = sys.stdin.readline
INF = int(1e8)


n, m = map(int, input().split())
dp = [[INF]*n for _ in range(n)]
mid = n // 2 + 1

for i in range(n):
    dp[i][i] = 0

for _ in range(m):
    x, y = map(int, input().split())
    dp[x-1][y-1] = 1

# 플로이드 워샬
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

answer = 0

# 진출차수 - 본인보다 큰 구슬의 개수
for row in dp:
    count = [k for k in row if k != INF]
    if len(count) > mid:
        answer += 1

# 진입차수 - 본인보다 작은 구슬의 개수
for j in range(n):
    column = [row[j] for row in dp]
    count = [k for k in column if k != INF]
    if len(count) > mid:
        answer += 1

print(answer)
