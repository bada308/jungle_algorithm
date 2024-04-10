'''
https://www.acmicpc.net/problem/2294
동전2
'''

import sys
input = sys.stdin.readline
INF = int(1e8)

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] + [INF for _ in range(k)]

for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
