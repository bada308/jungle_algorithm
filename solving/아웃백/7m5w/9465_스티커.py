'''
https://www.acmicpc.net/problem/9465
'''
import sys
input = sys.stdin.readline

t = int(input())

for __ in range(t):
    n = int(input())
    stickers = [[0] + list(map(int, input().split())) for __ in range(2)]
    dp = [[0] * (n + 1) for __ in range(2)]
    dp[0][1], dp[1][1] = stickers[0][1], stickers[1][1]

    for i in range(2, n+1):
        for j in range(2):
            if j == 0:
                dp[j][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[j][i]
            else:
                dp[j][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[j][i]
    print(max(dp[0][-1], dp[1][-1]))