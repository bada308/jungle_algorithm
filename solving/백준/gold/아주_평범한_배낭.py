'''
https://www.acmicpc.net/problem/12865
평범한 배낭
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
objects = [None] + [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, value = objects[i]
    for j in range(1, k+1):
        if weight > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)

print(dp[-1][-1])